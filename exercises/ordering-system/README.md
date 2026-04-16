# Ordering System (Python)

A streamlined command-line interface (CLI) application designed to simulate a real-world digital ordering process.

---

## 📌 Overview

This project focuses on mastering backend logic fundamentals. The primary objective was to implement a structured data flow using core Python concepts to handle transactions from selection to final receipt.

### Core Concepts Practiced:
- Modular Programming: Using dedicated functions for specific logic  
- Nested Data Structures: Managing complex data via lists of dictionaries  
- Control Flow: Utilizing loops and conditionals for user interaction  

---

## 🚀 Features
- Dynamic Menu: Browse items with real-time price mapping  
- Order Management: Build a persistent list of selected items during the session  
- Financial Logic: Automatic subtotal calculation with a 15% tax application  
- Detailed Summary: Final output provides a clean breakdown of items and costs  

---

## 📊 Data Structures

### Menu Mapping
The menu is stored as a dictionary, allowing for quick O(1) lookups via item IDs.

```python
menu = {
    1: {"name": "espresso", "price": 1.99},
    2: {"name": "coffee", "price": 2.50},
    3: {"name": "cake", "price": 2.79},
}

### Order List

User selections are stored in a list of dictionaries to maintain the order of selection.

order = [
    {"name": "espresso", "price": 1.99},
    {"name": "cake", "price": 2.79}
]

| Function                    | Responsibility                                                                |
| --------------------------- | ----------------------------------------------------------------------------- |
| `calculate_subtotal(order)` | Iterates through the order list and returns a sum rounded to 2 decimal places |
| `calculate_tax(subtotal)`   | Applies a flat 15% tax rate to the provided subtotal                          |
| `summarize_order(order)`    | Coordinates the subtotal and tax logic to generate a final receipt            |



 ## 🛠️ Program Flow
User Input →  Items Selection
        ↓
Build Order List
        ↓
Calculate Subtotal
        ↓
Apply 15% Tax
        ↓
Return Final Summary


## 💡 Key Takeaways
- Separation of Concerns: Decoupled calculation logic from user input logic
- Data Integrity: Practiced rounding and formatting floats for financial accuracy
- IPO Model: Reinforced the Input → Processing → Output mental model