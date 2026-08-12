import json

# ==========================================
# 1. ACTUAL PYTHON FUNCTIONS
# ==========================================

def calculate(operation: str, x: float, y: float) -> float:
    """Performs basic arithmetic operations."""
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        if y == 0:
            return "Error: Division by zero"
        return x / y
    else:
        return f"Error: Unknown operation '{operation}'"

def lookup_order_status(order_id: str) -> str:
    """Mock database lookup for an e-commerce order."""
    mock_db = {
        "ORD-123": {"status": "Shipped", "carrier": "FedEx", "tracking": "FX99281"},
        "ORD-456": {"status": "Processing", "carrier": "Pending", "tracking": "N/A"},
    }
    
    order = mock_db.get(order_id)
    if order:
        return json.dumps(order)
    return json.dumps({"error": "Order ID not found."})

# ==========================================
# 2. TOOL DISPATCHER (Router)
# ==========================================

def execute_tool(tool_name: str, arguments: dict):
    """Routes the LLM's request to the correct local function."""
    print(f"\n[SYSTEM] Executing Tool: {tool_name} with args {arguments}")
    
    if tool_name == "calculate":
        return str(calculate(arguments.get("operation"), arguments.get("x"), arguments.get("y")))
    elif tool_name == "lookup_order_status":
        return lookup_order_status(arguments.get("order_id"))
    else:
        return f"Error: Tool {tool_name} not found."

# ==========================================
# 3. JSON SCHEMAS FOR THE LLM
# ==========================================

AGENT_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform basic math operations (add, subtract, multiply, divide).",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {"type": "string", "enum": ["add", "subtract", "multiply", "divide"]},
                    "x": {"type": "number", "description": "The first number"},
                    "y": {"type": "number", "description": "The second number"}
                },
                "required": ["operation", "x", "y"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "lookup_order_status",
            "description": "Look up the shipping status and tracking info for an order.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {"type": "string", "description": "The order ID, e.g., 'ORD-123'"}
                },
                "required": ["order_id"]
            }
        }
    }
]
