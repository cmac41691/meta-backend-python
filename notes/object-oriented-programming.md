# Object-Oriented Programming (OOP)

## Overview
- OOP organizes code using objects and classes
- Focuses on modeling real-world entities
- Combines data (attributes) and behavior (methods)

---

## Key Concepts

### Class
- Blueprint for creating objects
- Defines attributes and methods

### Object
- Instance of a class
- Has its own data

### Attribute
- Variables inside a class
- Represent data

### Method
- Functions inside a class
- Define behavior

---

## Python Classes and Instances

### Basic Structure

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello " + self.name)

### Creating an Object
p1 = Person("Coady")
p1.greet()

### init Method
- Special method (constructor)
- Runs when object is created
- Used to initialize data

### self Keyword
- Refers to the current object
- Used to access attributes and methods

### Exercise: Define a Class
## Goal
- Create a class
- Add attributes
- Add at least one method


### Key Takeaways
- Classes are blueprints for objects
- Objects are instances of a class
- __init__ sets up object data
- self connects data to methods
- Classes are used in backend systems to model entities (e.g., User, Order, Product)   