def validate_password(password: str) -> bool:
    if not isinstance(password, str):
        return False

    # Count length manually
    length = len(password)

    if length < 8 or length > 20:
        return False

    # Flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    invalid_chars = [' ', '<', '>', '{', '}']

    repeat_count = 1
    prev_char = ''

    i = 0
    while i < length:
        ch = password[i]
        if ch in invalid_chars:
            return False
        if '0' <= ch <= '9':
            has_digit = True
        if 'a' <= ch <= 'z':
            has_lower = True
        if 'A' <= ch <= 'Z':
            has_upper = True

        if ch in special_chars:
            has_special = True
        if ch == prev_char:
            repeat_count += 1
            if repeat_count > 2:
                return False
        else:
            repeat_count = 1

        prev_char = ch
        i += 1

    return has_upper and has_lower and has_digit and has_special
