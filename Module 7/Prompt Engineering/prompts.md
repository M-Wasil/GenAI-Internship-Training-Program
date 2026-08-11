## 1. Summarization

### ❌ Before

> Summarize this customer review for our team.

### ✅ After

> **Role:** You are a customer experience analyst.
> **Task:** Provide a concise summary of the customer review provided below.
> **Constraints:**
> * Keep the summary under 3 sentences.
> * Highlight the core issue and any product mentioned.
> * Maintain an objective, neutral tone.
> 
> 
> **Input Review:**
> ```text
> [Insert customer review text here]  
> 
> ```
> 
> 
> **Output Format:**
> * **Core Issue:** [1 sentence summary]
> * **Product Mentioned:** [Product name or N/A]
> * **Recommended Action:** [1 brief sentence]
> 
> 

### 💡 What Improved

* **Persona & Guardrails:** Gives the model a clear analytical perspective and caps output length to prevent rambling.
* **Delimiters:** Wraps input text in code blocks to prevent prompt injection or confusion.
* **Structured Output:** Enforces a consistent, key-value format for quick team reading.

---

## 2. Text Classification

### ❌ Before

> Is this email spam, support, or sales?

### ✅ After

> **Role:** You are an automated email triage assistant.
> **Task:** Classify the incoming email into exactly ONE of the following predefined categories:
> 1. `Support` - Technical issues, bugs, account help, or product questions.
> 2. `Sales` - Pricing inquiries, demo requests, partnership proposals.
> 3. `Spam` - Unsolicited promotional offers, phishing, or irrelevant content.
> 
> 
> **Instructions:**
> * Choose only from the three categories listed above.
> * Output JSON format only with no extra introductory text or markdown wrappers outside the JSON.
> 
> 
> **Input Email:**
> ```text
> [Insert incoming email body here]  
> 
> ```
> 
> 
> **Output JSON Structure:**
> ```json
> {  
>   "category": "Support | Sales | Spam",  
>   "confidence_score": 0.0 to 1.0,  
>   "reasoning": "One sentence explaining why."  
> }  
> 
> ```
> 
> 

### 💡 What Improved

* **Explicit Definitions:** Defines edge cases and boundaries for each class to reduce ambiguity.
* **Schema Enforcement:** Generates strict JSON, making it ready to parse downstream in automated pipelines.
* **Confidence Scoring:** Asks for reasoning and a confidence score to aid human review when uncertainty is high.

---

## 3. Information Extraction

### ❌ Before

> Extract the details from this invoice text.

### ✅ After

> **Task:** Extract key financial and vendor details from the unstructured invoice text below.
> **Extraction Rules:**
> * If a field is missing or cannot be inferred, set its value to `null`.
> * Standardize all dates to `YYYY-MM-DD`.
> * Express monetary values as numbers without currency symbols (e.g., `150.00`).
> 
> 
> **Input Document:**
> `<invoice>`
> [Insert raw invoice text here]
> `</invoice>`
> **Output Format (JSON):**
> ```json
> {  
>   "vendor_name": string or null,  
>   "invoice_number": string or null,  
>   "invoice_date": "YYYY-MM-DD" or null,  
>   "total_amount": number or null,  
>   "line_items": [  
>     {  
>       "description": string,  
>       "amount": number  
>     }  
>   ]  
> }  
> 
> ```
> 
> 

### 💡 What Improved

* **Data Normalization:** Enforces standard date and currency formats rather than raw text copies.
* **Null Handling:** Prevents model hallucinations when information is missing from the source text.
* **XML Tag Delimiters:** Prevents messy text boundaries with clear `<invoice>` tags.

---

## 4. Text Transformation & Formatting

### ❌ Before

> Rewrite this technical update email to sound better.

### ✅ After

> **Role:** You are a senior technical program manager.
> **Task:** Rewrite the internal technical update into a polished executive status update for non-technical stakeholders.
> **Guidelines:**
> * Translate deep technical jargon (e.g., database deadlock, low memory error) into business-impact language (e.g., temporary service slowdown, performance optimization).
> * Structure the response into clear, bulleted sections.
> * Tone should be professional, reassuring, and solution-focused.
> 
> 
> **Raw Update:**
> `"""`
> [Insert raw engineering notes/update here]
> `"""`
> **Format Template:**
> **Executive Summary:** [2 sentences]
> **Key Achievements / Progress:**
> * [Bullet point 1]
> * [Bullet point 2]
> **Impact & Next Steps:** [1-2 sentences]
> 
> 

### 💡 What Improved

* **Target Audience Definition:** Clarifies the audience (executives vs. technical staff) to calibrate tone and complexity.
* **Jargon Mapping:** Explicitly guides the model on how to translate technical details into business terms.

---

## 5. Few-Shot Reasoning & Calculation (Chain-of-Thought)

### ❌ Before

> Calculate the total price with tax and discount for these items.

### ✅ After

> **Task:** Compute the final charge for an order by step-by-step calculation.
> **Rules:**
> 1. Sum item subtotal.
> 2. Apply discount percentage to subtotal before tax.
> 3. Apply sales tax rate to discounted subtotal.
> 4. Round final output to 2 decimal places.
> 
> 
> **Example 1 (Few-Shot):**
> **Input:** Items: $100, Tax: 10%, Discount: 20%
> **Thinking:**
> * Subtotal = $100
> * Discount = 20% of $100 = $20
> * Discounted Subtotal = $100 - $20 = $80
> * Tax = 10% of $80 = $8
> * Total = $80 + $8 = $88.00
> **Output:** $88.00
> 
> 
> **Actual Input:**
> Items: [Insert item prices], Tax Rate: [Insert tax %], Discount: [Insert discount %]
> **Work through the steps systematically before providing the final answer:**

### 💡 What Improved

* **Few-Shot Demonstration:** Gives an explicit in-context example showing the required reasoning path.
* **Chain-of-Thought (CoT):** Forces the model to generate intermediate mathematical steps, reducing calculation errors.
