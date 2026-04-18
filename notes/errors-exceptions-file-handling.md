# Errors, Exceptions, and File Handling

## Overview

This section covers how Python handles errors, how to manage exceptions, and how to safely work with files.

---

## Errors vs Exceptions

* **Error** → something goes wrong in the program
* **Exception** → a type of error that can be handled without crashing

---

## Try / Except

### Purpose

Prevents the program from crashing when something goes wrong.

### Backend Thinking

User → sends input
Server → processes input
If input is invalid → handle error instead of crashing

### Example

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
```

---

## Common Exceptions

* `ValueError` → invalid input (e.g., text instead of number)
* `TypeError` → wrong operation on data type
* `ZeroDivisionError` → division by zero
* `FileNotFoundError` → file not found

---

## Finally Block

Runs no matter what happens:

```python
try:
    # code
except:
    # handle error
finally:
    print("This always runs")
```

---

## File Handling

### Opening Files

```python
file = open("data.txt", "r")
```

Modes:

* `"r"` → read
* `"w"` → write (overwrites file)
* `"a"` → append

---

## Best Practice (with open)

```python
with open("data.txt", "r") as file:
    content = file.read()
```

* Automatically closes the file
* Safer approach

---

## Key Takeaways

* Use try/except to prevent crashes
* Handle user input safely
* Use `with open` for file handling
* Errors are part of normal programming

---

## Mistakes / Gaps

* Need more practice with try/except
* Still learning exception types
* Need to remember file modes (r, w, a)

---

## Notes

* Errors help understand program flow
* Exception handling is important for backend systems
