# Password Validator

This project contains a Python implementation of a secure and rules-based password validator with an accompanying test suite.

---

## Features
The `validate_password()` function enforces the following rules:

1. **Length**: Password must be **8 to 20 characters** long (inclusive).
2. **Character Requirements**: Must include **at least one**:
   - Uppercase letter (`A-Z`)
   - Lowercase letter (`a-z`)
   - Digit (`0-9`)
   - Special character: one of `!@#$%^&*()`
3. **Invalid Characters**: Must **not contain** any of the following:
   - Spaces or the characters `<`, `>`, `{`, `}`
4. **Repetition Rule**: No character can appear **three or more times consecutively**.

---

## Testing

Tests are located in `test_password_validator.py` and use the `unittest` framework. To run the test suite:

```bash
python test_password_validator.py
```

---

## How to Run the Files

### 1. Run a Manual Test:
Add the following at the bottom of `password_validator.py` to test a single password manually:

```python
if __name__ == "__main__":
    print(validate_password("StrongPass1!"))
```
Then run:

```bash
python password_validator.py
```

### 2. Run All Unit Tests:

```bash
python test_password_validator.py
```

---

## Project Structure

```text
password_validator.py         # Password validation logic (no built-ins like re, len, etc.)
test_password_validator.py    # Unit tests using unittest
README.md                     # Project documentation
```

---

## Security Notes

- This validator avoids using built-in functions like `re`, `int()`, or `len()` to simulate a low-level environment.
- No timing or cryptographic guarantees are made — **not suitable for real-world password authentication** without further security considerations.

---