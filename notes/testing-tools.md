# Testing Tools

## What is Testing?

Testing verifies that code behaves as expected.

Purpose:
- Detect bugs early
- Validate logic
- Improve reliability
- Prevent broken code from reaching users

---

## Types of Testing

### Unit Testing
Tests small pieces of code independently.

Example:

```python
def add(a, b):
    return a + b
```

Test:

```python
assert add(2, 3) == 5
```

---

### Integration Testing
Tests how multiple components work together.

Example:

```text
User login
↓
Server
↓
Database
↓
Response
```

Checks whether these systems communicate correctly.

---

### System Testing

Tests the complete application.

Example:

```text
Open app
↓
Login
↓
Purchase item
↓
Receive confirmation
```

---

### Regression Testing

Checks whether new updates accidentally break older features.

Example:

```text
Added password feature
↓
Login suddenly breaks
↓
Regression test catches issue
```

---

## Backend Connection

Client
↓
Request
↓
Server
↓
Logic
↓
Testing
↓
Database
↓
Response

Testing acts as a safety checkpoint before production.

---

## Personal Connection

Current workflow:

Write code
↓
Run in Git Bash
↓
Check output manually

Future workflow:

Write code
↓
Write tests
↓
Run PyTest
↓
Automatic pass/fail