# Functional Programming Exercises

## Overview
This section focuses on practicing functional programming concepts in Python, including reversing strings, mapping values, filtering data, and using list comprehensions.

---

## Pseudocode

### Reverse String
INPUT string  
SET reversed_string = empty  

FOR each character in string (from end to start)  
    ADD character to reversed_string  

DISPLAY reversed_string  

---

### Map (Double Values)
SET digits = list of numbers  
SET result_list = empty  

FOR each number in digits  
    SET new_value = number * 2  
    ADD new_value to result_list  

DISPLAY result_list  

---

### Filter (Even Numbers)
SET digits = list of numbers  
SET evens = empty  

FOR each number in digits  
    IF number % 2 == 0  
        ADD number to evens  

DISPLAY evens  

---

## Implementation Notes

- Used loops to implement transformation and filtering
- Practiced building results step-by-step
- Compared loop-based approaches with Pythonic alternatives

---

## Examples

### Map (Double Values)

Input:
[3, 4, 8, 12]


Output:
[6, 8, 16, 24]


---

### Filter (Even Numbers)

Input:
[3, 4, 8, 12]


Output:
[4, 8, 12]


---

## Key Takeaways

- `map()` transforms each element in a collection
- `filter()` selects elements based on a condition
- List comprehensions provide a cleaner, more Pythonic approach
- Pseudocode helps break down logic before coding

---

## Comprehension Assignment

### Files
- `comprehension_assignment.py` → implementation  
- `comprehension_pseudocode.md` → planning  

### Goals
- Use `map()` to transform data  
- Use list comprehension for string formatting  
- Use dictionary comprehension for key-value mapping  

### Functions
- `to_mod_list()`  
- `generate_usernames()`  
- `map_id_to_initial()`  

### Key Takeaways
- `map()` applies a function to each element  
- List comprehensions simplify transformations  
- Dictionary comprehensions build mappings efficiently  

---

## Overall Insight

The same problems can be solved using both imperative (loops) and functional (map/comprehensions) approaches.  
Functional approaches tend to be more concise and expressive in Python.