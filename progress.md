## 2026-04-04

### Started
- Meta Backend - Programming in Python (Module 1)

### Focus
- Understanding Python’s role in backend systems
- Setting up development structure

### Notes
Beginning with fundamentals but framing everything as backend flow.


## 2026-04-06

### Completed
- Learned variables
- Learned basic data types
- Continued Python fundamentals

### Key Takeaways
- Variables store user data
- Input is always a string
- Data types affect how data is processed

### Reflection
Focused on understanding data flow and how backend systems store and process input.



## 2026-04-07

### Completed
- Type casting input assignment
- Converted input() to int and float
- Implemented boolean logic from user input
- Built bill calculator with formatted output

### Key Takeaways
- input() always returns string
- Must cast before calculations
- Float formatting is important for real-world data (money)

### Reflection
Focused on handling user input correctly and ensuring data is properly converted before processing.



## 2026-04-08

### Completed
- Knowledge Check – Welcome to Python Programming (80%)
- Reviewed math and logical operators
- Began control flow and conditionals module
- Built age classifier mini-project using if/elif/else

### Key Takeaways
- Conditions evaluate to True or False
- Control flow determines program behavior
- Comparison operators (>, <, ==, etc.) drive decisions
- Input must be converted before being used in logic

### Reflection
Started understanding how programs make decisions based on user input. Focused on connecting input → processing → output with conditional logic. Beginning to see how backend systems validate and route data.



## 2026-04-09

### Completed
- Math and logical operators
- Control flow (if / elif / else)
- Conditional statements
- Introduced loops (while)

### Key Takeaways
- Control flow determines program execution paths
- Logical operators combine conditions (and, or, not)
- while loops allow repeated validation
- Input should be validated before conversion

### Project Work
- Built a validated age classifier
- Implemented loop-based input validation
- Applied conditional branching for classification

### Notes
- Learned to avoid redundant variables
- Practiced clean input → validate → convert → use flow

## 2026-04-10

### Completed
- Match statement
- Looping constructs
- Practical loop examples
- Practicing control flow and loops

### Key Takeaways
- match statement provides cleaner branching for fixed options
- while loops enable continuous program flow
- break exits a loop, continue restarts the loop iteration
- loops + conditionals create interactive systems

### Project Work
- Built a menu-driven CLI system
- Integrated age classifier into menu flow
- Implemented routing using match-case
- Combined loops, conditionals, and validation into one system

### Notes
- Learned how to structure programs with multiple execution paths
- Understood that variables must be created before being used
- Practiced integrating existing logic into a larger system

## 2026-04-11

### Planned
- Python loops (dialogue)
- Nested loops and algorithmic complexity
- Control flow + loops problem exercise
- Review solution
- Self-review assignment
- Module summary 
- Module quiz

### Focus
- Understand nested loops (loop inside loop)
- Learn how loops affect performance (basic complexity thinking)
- Apply loops + conditionals together to solve problems
- Reinforce problem-solving workflow (pseudocode → code → test)

### Goal
- Complete Module 1
- Strengthen confidence with loops and control flow


### Completed
- Python loops (dialogue)
- Nested loops and algorithmic complexity
- Control flow + loops problem exercise
- Solution review
- Self-review assignment (100%)
- Module summary
- Module quiz (90%)

### Key Takeaways
- Loops control repeated execution
- Nested loops introduce layered processing
- break stops execution early
- enumerate provides index + value
- Control flow determines how programs behave

### Project Work
- Built loop-based number processing system
- Implemented enumerate for index tracking
- Applied conditional logic (>45 classification)
- Added break condition to stop at target value (36)
- Counted iterations before termination

### Notes
- Execution flow matters more than syntax
- Indentation defines logic structure in Python
- break affects total iterations and output

## 2026-04-12

### Completed
- Built user list manager CLI using functions and lists
- Implemented validation (empty input, duplicate check)
- Practiced control flow and function structure

### Key Takeaways
- Functions = reusable backend logic
- Lists simulate stored data
- Validation is critical before storing data

### Notes
- This felt like building a small backend system without HTTP
- First time separating logic into functions in a meaningful way

## 2026-04-15

### Completed
- Completed "Functions, loops and data structures" programming assignment
- Achieved 100% on first attempt
- Reinforced use of functions, loops, and data structures together

### Key Takeaways
- Functions organize logic into reusable units
- Loops control flow and repeated operations
- Data structures (lists, dicts, sets) define how data is stored and accessed
- Combining all three creates real backend-style logic

### Notes
- Assignment felt easier due to prior practice with CLI user manager
- Understanding improved by building before the assignment

## 2026-04-17

### Completed
- Programming Assignment: Functions, Loops, and Data Structures
- Built CLI ordering system with:
  - subtotal calculation
  - tax calculation
  - order summary function

### Result
- Passed: 85%

### Key Takeaways
- Functions should be self-contained and return values
- Proper indentation is critical in Python
- Lists of dictionaries are powerful for structured data
- Breaking problems into smaller functions makes logic easier

### Notes
- Debugged issues with indentation and variable scope
- Reinforced backend thinking: input → processing → output
- Practiced combining multiple functions into one workflow

## 2026-04-18

### Completed

* Knowledge Check: Functions and Data Structures (Score: 80%)
* What are exceptions
* Exception handling
* Exercise: Exceptions in Python
* Exceptions in Python – solution
* Exceptions in Python (Practice Assignment – 100%)
* File handling in Python (intro)

---

### Key Takeaways

* Exceptions prevent programs from crashing
* `try/except` allows safe handling of user input and runtime errors
* Different exception types handle different failure cases
* File handling introduces persistent data (read/write operations)

---

### Backend Thinking

Client → sends input
Server → processes input
If failure occurs → handle with exception
System continues running instead of crashing

File flow:
Client → request data
Server → open/read/write file
Response → return processed data

---

### Notes

* Reinforced importance of handling invalid user input
* Practiced using try/except blocks in real scenarios
* Learned how backend systems stay stable under failure
* Introduced to file operations (foundation for data persistence)

---

### Improvements (Next Step)

* Practice file reading and writing in a small CLI program
* Combine exception handling with file operations
* Prepare for upcoming assignment involving data storage

## 2026-04-19

### Completed
- Meta Backend Python Assignment (File Operations)
- Implemented file reading, writing, reversing, and filtering
- Passed all grader tests (100%)

### Key Takeaways
- Preserving raw data matters more than formatting in backend systems
- Newline characters (\n) can affect system validation
- Edge cases (empty input, indexing) must always be handled

### Notes
- Avoid using .strip() when exact output format is required
- file.readlines() is useful for preserving line structure  

## 2026-04-20

### Completed
- Meta Backend Python Assignment (File Operations)
- Implemented file reading, writing, reversing, and filtering
- Passed all grader tests (100%)

### Key Takeaways
- Backend systems often require exact data preservation over formatting
- Newline characters (\n) can affect system validation
- Edge cases (empty input, indexing) must always be handled

### Challenges
- Initially removed newline characters using .strip(), causing grader failures
- Debugged mismatch between expected vs actual output formatting

### Notes
- Avoid using .strip() when exact output format is required
- file.readlines() preserves exact line structure including newline characters

## 2026-04-25

### Completed
- Coffee procedural programming exercise
- Implemented full program using functions and control flow
- Structured project inside exercises/procedural-programming/coffee

### Key Takeaways
- Function order matters in execution
- Scope affects variable accessibility (NameError issues)
- Indentation defines program structure in Python
- Loops simulate real-world processes (heating, cooling)

### Notes
- Translated algorithm → working code
- Debugging was the main learning focus today

## 2026-04-29

### Completed
- Reverse string (loop + slicing)
- Map (loop + list comprehension)
- Filter (loop + list comprehension)

### Key Takeaways
- Functional programming emphasizes transformation over mutation
- List comprehensions are more concise and Pythonic
- Same logic can be expressed in multiple paradigms

### Notes
- Practiced translating pseudocode into both imperative and functional styles

## 2026-05-02

### Completed
- Functional Programming Assignment (Coursera) – 100%
- Implemented:
  - to_mod_list (map transformation)
  - generate_usernames (list comprehension)
  - map_id_to_initial (dictionary comprehension)

### Key Takeaways
- map() applies a function across a sequence
- list comprehensions simplify transformations
- dictionary comprehensions build key-value mappings efficiently
- same logic can be expressed in loop-based and Pythonic styles

### Notes
- Built loop-based versions first for understanding
- Then implemented Pythonic versions for assignment submission
- Confirmed outputs locally before submission


## 2026-05-04

### Focus
- OOP Principles (reading)
- Python Classes and Instances (video)

### Plan
- Review OOP notes (object-oriented-programming.md)
- Write down key concepts in notebook:
  - class vs object
  - attributes vs methods
  - __init__ and self
- Watch video and connect concepts to code examples

### Goal
- Understand how classes and objects work conceptually
- Be comfortable reading basic class syntax 

## 2026-05-08

### Completed
- Instantiate a custom object
- Object instantiation self-review
- Practiced class construction and method calls
- Explored custom object behavior beyond assignment requirements

### Exercises
- Created MyFirstClass practice exercise
- Experimented with:
  - class variables
  - method parameters
  - object creation
  - constructor behavior
  - method output formatting

### Key Takeaways
- Objects are created from classes
- Methods define object behavior
- self references the current instance
- Constructors initialize object state
- Class variables can be shared across all objects

## 2026-05-09

### Completed
- Practiced instance methods
- Built Payslip class exercise
- Practiced object state updates
- Explored parent and child classes
- Implemented inheritance with HumanResources and Recruiter classes
- Practiced using super().__init__()

### Exercises
- instance_method_exploration.py
- parent_child_exploration.py

### Key Takeaways
- Child classes inherit parent behavior
- super() reuses parent constructor logic
- Instance methods modify object state
- Objects can share behavior while storing unique data
- Indentation and scope directly affect class structure

## 2026-05-10

### Completed
- Abstract classes and methods assignment
- Practiced inheritance and method overriding
- Implemented abstract base classes using ABC
- Built Swiss bank withdrawal system
- Added insufficient funds edge-case handling
- Created pseudocode planning document
- Submitted assignment locally and on Coursera

### Key Takeaways
- Abstract classes define required methods for child classes
- Child classes override parent behavior
- Instance variables preserve object state
- Conditional checks help protect backend logic
- Pseudocode improves implementation flow

### Git / Repo Work
- Added bank_assignment.py
- Added bank_pseudocode.md
- Cleaned duplicate file naming issue
- Committed and pushed assignment work

## 2026-05-11

### Completed
- Method Resolution Order
- Working with Methods: Examples

### Key Takeaways
- Python searches for methods using MRO
- Child class methods override parent methods
- super() allows access to parent functionality
- Instance methods operate on object state through self

### Module 3 Wrap-Up
- Completed object-oriented programming fundamentals
- Practiced inheritance and abstract classes
- Improved understanding of method resolution and object behavior
- Continued building backend thinking through class-based design

## 2026-05-15

### Completed
- Began Module 4: Modules and Packages
- Learned how Python modules expose reusable functionality
- Practiced importing standard library modules (`sys`, `calendar`)
- Explored `sys.path` and iterated through system locations
- Used `calendar.leapdays()` and `calendar.isleap()`
- Created `modules-packages/` directory structure
- Added initial Module 4 exercise files
- Implemented `import_examples.py`

### Key Takeaways
- Python modules contain reusable functions, attributes, and tools
- Module functionality is accessed through:
  - `module.attribute`
  - `module.function()`
- Imports help organize and separate reusable logic
- Backend systems rely heavily on modular architecture and imported functionality
- Debugging variable consistency and module relationships is important

### Reflection
Today focused on understanding how Python modules work and how applications access reusable functionality from imported modules. I practiced using `sys` and `calendar` while reinforcing loops, variable storage, and module-function relationships. I also reorganized the repository structure to better reflect Module 4 concepts and backend-oriented organization.

## 2026-05-16

### Completed
- Continued Module 4: Modules and Packages
- Learned about import statements and aliasing
- Created examples using:
  - `import math`
  - `from math import sqrt as m`
- Added import examples to `modules-packages/import_examples.py`
- Began learning namespacing and scope concepts
- Practiced writing custom scope pseudocode

### Key Takeaways
- Modules expose reusable functionality
- Imports can bring in entire modules or specific functions
- Aliases provide shorter or custom names for imported functionality
- Namespaces help organize ownership of variables and functions
- Scope controls where variables can be accessed and modified

### Reflection
Today focused on understanding how Python organizes and accesses functionality. I practiced imports and aliases and began exploring scope and namespaces through pseudocode. I am starting to think more about where data belongs and how different parts of a program communicate with each other rather than only focusing on syntax.

## 2026-05-18

### Completed
- Import and scope assignment
- Created employee dictionary with function parameters
- Implemented JSON file output
- Generated employee.json successfully
- Tested locally using Git Bash

### Debugging / Fixes
- Fixed import issues
- Fixed create_dict() argument mismatch
- Fixed accidental OVR overwrite mode in VS Code
- Fixed indentation and main() flow
- Verified JSON artifact generation

### Key Takeaways
- Functions with parameters require matching arguments
- json.dump() writes to files
- json.dumps() converts dictionaries into JSON strings
- Testing locally helps catch issues before submission

## 2026-05-18

### Completed
- Finished Module 4 Import and Scope programming assignment
- Built employee JSON generator project
- Practiced importing variables and functions from external modules
- Created employee dictionary using function parameters
- Converted Python dictionary into JSON format using `json.dumps()`
- Wrote JSON output to `employee.json`
- Debugged import issues and function parameter problems
- Resolved Coursera autograder edge-case failures
- Submitted assignment successfully
- Scored 100/100 on Import and Scope assignment

### Challenges
- Import errors caused by variable naming mismatches
- Function arguments initially depended on local variables instead of passed parameters
- Coursera test cases failed despite local code working
- Needed to adjust implementation for strict autograder expectations

### Key Takeaways
- Functions should rely on passed arguments rather than hardcoded values
- Local success does not always guarantee external test success
- `json.dumps()` converts Python objects into JSON strings
- `file.write()` writes the JSON string directly into the output file
- Autograders often test unexpected inputs and edge cases
- Debugging is frequently about identifying assumptions in code

### Reflection
Today felt closer to real backend debugging than just completing an exercise.
The code worked locally, but the testing environment exposed assumptions that I had built into the implementation. I had to progressively refine imports, parameters, typecasting, and file handling until the solution became flexible enough to pass external tests. Working through the failures step-by-step improved my understanding of how modules and function design work together.


## 2026-05-21

### Completed
- reload() function lesson
- Module use-cases reading
- Additional resources
- Knowledge check
- Built and tested reload_demo.py locally
- Created filechanges.py module

### Key Takeaways
- Learned how importlib.reload() works
- Practiced dynamic module reloading
- Improved Python indentation consistency
- Better understanding of module imports and execution flow
- Practiced try/except structure with reload logic

## 2026-05-22

### Completed
- Created `popular-packages-and-frameworks` directory
- Added README.md structure
- Defined planned topics:
  - NumPy
  - pandas
  - Matplotlib
  - Data analysis packages
  - Machine learning / AI libraries
  - Python web frameworks
- Established learning goals for the subsection
- Prepared repository structure for upcoming exercises and notes

### Key Takeaways
- Continued repository organization
- Prepared workspace before implementation
- Breaking larger modules into smaller sections makes learning easier to manage

## 2026-05-23

### Completed
- Finished introductory package/framework content
- Created beginner demo files:
  - numpy_demo.py
  - pandas_demo.py
  - matplotlib_demo.py
- Installed Python packages:
  - NumPy
  - pandas
  - Matplotlib
- Upgraded pip successfully
- Verified packages using:
  python -m pip list

### Key Takeaways
- Packages extend Python with specialized functionality
- NumPy works with arrays and numerical operations
- pandas structures data like tables/spreadsheets
- Matplotlib creates graphs and visualizations
- Practiced reading terminal errors and correcting commands

## 2026-05-24

### Completed
- Finished Popular Packages, Libraries and Frameworks subsection
- Learned about:
  - Big Data and analysis tools
  - AI and Machine Learning concepts
  - Python web frameworks
- Participated in AI vs Machine Learning discussion
- Completed knowledge check (80%)
- Reviewed additional resources

### Key Takeaways
- Packages extend Python with specialized functionality
- Machine Learning is a method used within AI systems
- Frameworks provide structure and reduce repetitive code
- Backend frameworks help organize requests, logic, and responses 

## 2026-05-25

### Completed
- What is testing?
- Types of testing

### Key Takeaways
- Testing verifies that code behaves as expected.
- Testing helps detect bugs before software reaches users.
- Different testing types serve different purposes:
  - Unit testing → tests small pieces of code
  - Integration testing → tests how components work together
  - System testing → tests the full application
  - Regression testing → checks if new changes break existing features
- Testing fits into backend systems by validating logic before deployment.

### Backend Connection
Client → Request → Server → Logic → Testing → Database → Response

Testing acts as a safety checkpoint before code moves into production. 

## 2026-05-26

### Completed
- Testing quiz
- Test automation packages

### Key Takeaways
- Automated testing reduces repetitive manual checking.
- Testing tools can quickly verify whether code still works after changes.
- Automation helps developers catch bugs faster and improves software reliability.
- Testing frameworks are important in backend systems where many components interact together.

### Backend Connection
Without automation:
Write code → Run manually → Check output

With automation:
Write code → Run tests → Automatic pass/fail feedback

Automated testing improves development speed and stability in production systems. 



## 2026-05-27

### Completed
- Learned basic PyTest workflow
- Installed PyTest with pip
- Created:
  - addition.py
  - test_addition.py
- Wrote automated tests for:
  - addition
  - subtraction
- Ran tests successfully using pytest

### Key Takeaways
- PyTest automatically discovers files beginning with test_
- Assertions verify expected behavior automatically
- Testing helps validate backend logic before deployment
- Automated testing reduces manual debugging

### Backend Connection
Client → Request → Logic → Testing → Validation → Deployment

Testing acts as an automated verification layer for backend systems.

## 2026-05-31

### Completed
- PyTest string validation assignment
- String length testing
- String structure testing
- Fixtures
- Assertions
- Reading PyTest error output

### Challenges
- Confusion between spellcheck.py and test_spellcheck.py
- Fixture usage errors
- Assertion failures caused by test data
- Understanding PyTest collection behavior

### Key Takeaways
- Test files contain the assertions.
- Application files contain the implementation.
- PyTest error messages point directly to failing assertions.
- Fixing one error often reveals the next issue.
- Passing tests confirm expected behavior.

### Result
- Assignment submitted successfully
- Grade: 100/100
- Local verification: 2 passed


### 2026-06-05

#### Completed

- Recreated TDD example from video without copying
- Converted Python example into pseudocode first
- Built `findstring.py`
- Built `test_findstring.py`
- Practiced PyTest assertions
- Debugged indentation errors
- Investigated import/module errors
- Removed unsupported `curses.ascii` import on Windows
- Tested both passing and failing cases
- Used `"N7"` to intentionally observe assertion failure behavior
- Corrected test data and achieved passing results
- Successfully ran PyTest with all tests passing (`2 passed`)

#### Challenges

- Python indentation and block structure
- Undefined variable errors (`person`, `names`)
- Module import compatibility on Windows
- Understanding why assertions failed with invalid test data
- Translating pseudocode back into working Python

#### Key Takeaways

- PyTest reports exactly which assertion failed
- Failing tests help verify expected behavior
- Indentation is critical in Python functions
- TDD involves writing behavior checks before trusting code
- Test data must match the expected behavior of the function
- Import errors can occur due to operating system differences
- Debugging is often a process of fixing one issue at a time

#### Result

- Successfully recreated and implemented the course TDD example independently
- All PyTest tests passing (`2 passed`)
- Improved understanding of assertions, testing workflows, and debugging practices

### Additional Achievements
- Completed Module 4: Modules, Packages, Libraries and Tools
- Scored 87.5% on Module 4 quiz
- Completed testing subsection and TDD introduction

## 2026-06-07

### Completed

- Completed Programming in Python final graded assessment
- Passed course and earned Meta Programming in Python certificate
- Reviewed assessment feedback and reinforced weak areas
- Practiced dictionary lookups and PyTest-style test planning
- Updated LinkedIn certification profile
- Added repository to LinkedIn Featured section

### Key Takeaways

- Dictionaries iterate over keys by default
- Method Resolution Order (MRO) remains an important OOP concept
- Testing requires thinking about valid, invalid, and edge-case inputs
- PyTest assertions are useful for verifying expected behavior
- Backend development relies heavily on writing reliable and testable code

### Result

- Successfully completed Meta Programming in Python
- Ready to begin the next course in the Meta Back-End Developer Professional Certificate
- Built and validated a custom dictionary lookup project using PyTest (5 passing tests) 
