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
