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
- Compared loop-based approach with Pythonic alternatives

---

## Key Takeaways

- `map` transforms data
- `filter` selects data based on conditions
- list comprehensions provide a cleaner, more Pythonic approach
- pseudocode helps break down logic before coding