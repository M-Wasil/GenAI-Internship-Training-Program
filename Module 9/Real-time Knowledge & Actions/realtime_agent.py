import os
import json
import sqlite3
import urllib.request
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (.env file)
load_dotenv()

# ==========================================
# 1. DATABASE SETUP (SQLite)
# ==========================================
DB_FILE = "market_records.db"

def init_db():
    """Initializes the SQLite database table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_name TEXT NOT NULL,
            price_usd REAL NOT NULL,
            notes TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ==========================================
# 2. REAL-TIME & DB TOOLS IMPLEMENTATION
# ==========================================

def fetch_realtime_crypto_price(crypto_id: str) -> str:
    """Fetches real-time price data from CoinGecko API."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id.lower()}&vs_currencies=usd"
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if crypto_id.lower() in data:
                price = data[crypto_id.lower()]["usd"]
                return json.dumps({"asset": crypto_id, "price_usd": price, "status": "success"})
            else:
                return json.dumps({"error": f"Crypto '{crypto_id}' not found."})
    except Exception as e:
        return json.dumps({"error": f"Failed to fetch data: {str(e)}"})

def save_record_to_db(asset_name: str, price_usd: float, notes: str) -> str:
    """Inserts a real-time record into the local SQLite database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO crypto_logs (asset_name, price_usd, notes) VALUES (?, ?, ?)",
            (asset_name, price_usd, notes)
        )
        conn.commit()
        record_id = cursor.lastrowid
        conn.close()
        return json.dumps({"status": "success", "inserted_id": record_id, "message": f"Saved {asset_name} record to DB."})
    except Exception as e:
        return json.dumps({"status": "error", "message": str(e)})

def read_db_records() -> str:
    """Queries and returns the latest 5 records saved in the SQLite database."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT id, asset_name, price_usd, notes, timestamp FROM crypto_logs ORDER BY id DESC LIMIT 5")
        rows = cursor.fetchall()
        conn.close()
        
        records = [
            {"id": row[0], "asset": row[1], "price_usd": row[2], "notes": row[3], "timestamp": row[4]}
            for row in rows
        ]
        return json.dumps({"latest_records": records})
    except Exception as e:
        return json.dumps({"error": str(e)})

# Dispatcher function to route tool names to function code
def execute_tool(tool_name: str, arguments: dict) -> str:
    print(f"\n[AGENT ACTION] Calling tool '{tool_name}' with arguments: {arguments}")
    if tool_name == "fetch_realtime_crypto_price":
        return fetch_realtime_crypto_price(arguments.get("crypto_id"))
    elif tool_name == "save_record_to_db":
        return save_record_to_db(arguments.get("asset_name"), arguments.get("price_usd"), arguments.get("notes"))
    elif tool_name == "read_db_records":
        return read_db_records()
    else:
        return json.dumps({"error": f"Unknown tool '{tool_name}'"})

# ==========================================
# 3. JSON SCHEMAS FOR TOOLS
# ==========================================
TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "fetch_realtime_crypto_price",
            "description": "Fetch the current real-time USD price of a cryptocurrency (e.g., 'bitcoin', 'ethereum', 'solana').",
            "parameters": {
                "type": "object",
                "properties": {
                    "crypto_id": {"type": "string", "description": "The API identifier for the crypto, e.g. 'bitcoin' or 'ethereum'"}
                },
                "required": ["crypto_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "save_record_to_db",
            "description": "Write a financial asset log entry into the local SQLite database.",
            "parameters": {
                "type": "object",
                "properties": {
                    "asset_name": {"type": "string", "description": "Name of the asset"},
                    "price_usd": {"type": "number", "description": "Current price in USD"},
                    "notes": {"type": "string", "description": "Contextual note or calculation details"}
                },
                "required": ["asset_name", "price_usd", "notes"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_db_records",
            "description": "Fetch the latest saved records from the database to confirm writes.",
            "parameters": {"type": "object", "properties": {}}
        }
    }
]

# ==========================================
# 4. MULTI-STEP REACT AGENT LOOP
# ==========================================

# Configure API Client (Supports OpenRouter, Groq, or OpenAI)
api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("GROQ_API_KEY")
base_url = "https://openrouter.ai/api/v1" if os.getenv("OPENROUTER_API_KEY") else None

client = OpenAI(api_key=api_key, base_url=base_url)
MODEL_NAME = "openai/gpt-oss-20b:free" if os.getenv("OPENROUTER_API_KEY") else "gpt-4o-mini"

def run_realtime_agent(user_prompt: str, max_iterations: int = 6):
    print(f"\n================ USER PROMPT ================\n{user_prompt}\n=============================================")
    
    messages = [
        {"role": "system", "content": "You are an autonomous market-analysis agent. Use tools to fetch real-time data, do multi-step calculations, and persist results to the database."},
        {"role": "user", "content": user_prompt}
    ]

    for iteration in range(1, max_iterations + 1):
        print(f"\n--- [Iteration {iteration}] Calling LLM ---")
        
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=TOOLS_SCHEMA,
            tool_choice="auto"
        )
        
        message = response.choices[0].message
        messages.append(message)

        # Check if the model triggered any tool calls
        if message.tool_calls:
            for tool_call in message.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                
                # Execute tool and capture observation
                observation = execute_tool(function_name, arguments)
                print(f"[OBSERVATION]: {observation}")

                # Feed observation back to conversation history
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": observation
                })
        else:
            # Model didn't call a tool -> Task finished
            print(f"\n================ FINAL AGENT RESPONSE ================\n{message.content}")
            break

# ==========================================
# 5. EXECUTION ENTRY POINT
# ==========================================
if __name__ == "__main__":
    # Multi-step instruction testing live fetch + calculations + database persistence
    task_prompt = (
        "Check the real-time live prices for both 'bitcoin' and 'ethereum'. "
        "Calculate the average price of these two assets. "
        "Then, save both asset records into the database with a note containing the computed average price. "
        "Finally, query the database to verify the saved records."
    )
    
    run_realtime_agent(task_prompt)
