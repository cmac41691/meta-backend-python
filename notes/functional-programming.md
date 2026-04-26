# Functional Programming (Module 3)

## What is Functional Programming?

Functional programming is a paradigm where:
- functions are treated like values
- functions do not change state
- focus is on input → output

Key idea:
Same input → always same output

---

## Pure Functions

A pure function:
- does NOT modify external data
- does NOT rely on outside variables
- always returns the same result for the same input

Example (pure):
```python
def add(a, b):
    return a + b

Not pure:

total = 0

def add_to_total(x):
    global total
    total += x

## Why Pure Functions Matter (Backend Thinking)
- predictable behavior
- easier to debug
- easier to test
- safer in large systems        

## Recursion

Recursion = a function calling itself

Structure:

1) Base case (stop condition)
2) Recursive case (call itself)

Example:

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

## Tower of Hanoi (Concept)
- classic recursion problem
- move disks between rods
- requires breaking problem into smaller steps

Key takeaway:
Recursion solves problems by reducing them step-by-step

## Reversing a String

Iterative:

text = "hello"
print(text[::-1])

Recursive:
def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

map() and filter()

These work on collections (lists)

map():
Applies a function to every item
numbers = [1, 2, 3]
result = list(map(lambda x: x * 2, numbers))

Output:
[2, 4, 6]

filter():
Filters items based on a condition
numbers = [1, 2, 3, 4]
result = list(filter(lambda x: x % 2 == 0, numbers))

Output:
[2, 4]

Comprehensions

Cleaner alternative to map/filter

List comprehension:

numbers = [1, 2, 3]
result = [x * 2 for x in numbers]

With condition:
numbers = [1, 2, 3, 4]
evens = [x for x in numbers if x % 2 == 0]

## Functional Programming vs Procedural

Procedural:

- step-by-step instructions
- uses state changes
- loops

Functional:

- input → output focus
- avoids state changes
- uses transformations and recursion

## Key Takeaways     

- Functional programming focuses on data transformation
- Pure functions = predictable and safe
- Recursion = breaking problems down
- map/filter/comprehensions = working with collections

