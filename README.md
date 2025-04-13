# 🔐 Password Validator

This project contains a Python implementation of a secure and rules-based password validator with an accompanying test suite using **Pytest**.

---

## 🚀 Features

The `validate_password()` function enforces the following rules:

1. **Length**: Password must be **8 to 20 characters** long.
2. **Character Requirements**: Must include **at least one**:
   - Uppercase letter (`A-Z`)
   - Lowercase letter (`a-z`)
   - Digit (`0-9`)
   - Special character: one of `!@#$%^&*()`
3. **Invalid Characters**: Must **not contain**:
   - Spaces or the characters `<`, `>`, `{`, `}`
4. **Repetition Rule**: No character can appear **three or more times consecutively**.

---

## 🧪 Testing with Pytest

### ▶️ Run All Tests:

```bash
pytest
```
### ▶️ Install Pytest (if not already):

```bash
pip install pytest
```

### 📂 Test File:

Tests are located in:

```text
test_password_validator.py
```

Pytest will automatically discover and run all functions starting with `test_`.

---

## 🧰 How to Run Files

### 1. Manual Test:

You can manually test a password in `password_validator2.py`:

```python
if __name__ == "__main__":
    print(validate_password("StrongPass1!"))
```

Then run:

```bash
python password_validator2.py
```

### 2. Run Test Suite:

```bash
pytest
```

or specifically:

```bash
pytest test_password_validator.py
```

---

## 📁 Project Structure

```text
password_validator2.py         # Password validation logic
test_password_validator.py     # Pytest test suite
README.md                      # Project documentation
```

---

## 🔒 Security Notes

- This validator avoids using built-in libraries like `re`, `int()`, or `len()` to simulate low-level logic.
- It is designed for **educational/demo purposes** and is **not production-grade** for secure password handling.

---
```

You can save this content directly as your `README.md` file.

Let me know if you want to include GitHub badges, workflow instructions, or a sample test report as well!