# Control Flow and Conditionals

## Core Idea
Programs make decisions based on conditions (True / False).

## Syntax

if condition:
    # runs if true

elif condition:
    # runs if previous is false

else:
    # runs if all conditions are false

## Example

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

## Key Takeaways
- Conditions return True or False
- Code flow depends on decisions
- Used in validation and logic

## Backend Thinking
- Used for login checks
- Input validation
- Decision-making systems

## Match Statement
- Used for comparing a single value against multiple cases
- Cleaner than multiple elif statements in some scenarios

## Looping Constructs

### while loop
- Runs while condition is True
- Used for validation and repeated input

### for loop
- Iterates over a sequence (range, list, etc.)

## Practical Looping
- Counting iterations
- Processing multiple values
- Menu systems
- Repeating tasks until completion

## Backend Thinking
- Request retries
- Input validation loops
- Processing collections of data
- Task automation

## Reflection