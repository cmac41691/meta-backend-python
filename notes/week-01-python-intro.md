# Week 01 - Python Introduction

## Topics Covered
- Introduction to Python
- Control flow
- Conditionals

---

## TLDR

- Python is used as backend logic layer
- Handles input → processing → output
- Control flow determines how the system behaves based on conditions

---

## Backend Mapping

Client → Request → Server (Python) → Logic (if/else) → Response

- input() = request data
- if/else = decision logic
- print() = response

---

## Key Concepts

### Control Flow
Controls how the program executes step-by-step.

### Conditionals (if/else)
Used to make decisions based on input.

Example use case:
- Validate user input
- Check login credentials
- Route logic based on conditions

### Example (Backend Scenario)

Client sends request with user input

IF input is empty:
- server returns error response

ELSE:
- server processes input
- returns success response

## Reflection (Short)

Even basic conditionals are core backend logic.
Every API endpoint relies on decision-making like this.