def validate_password(password: str) -> bool:
    if not isinstance(password, str):
        return False

    # Count length manually
    length = 0
    for _ in password:
        length += 1

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
        for ic in invalid_chars:
            if ch == ic:
                return False
        if '0' <= ch <= '9':
            has_digit = True
        if 'a' <= ch <= 'z':
            has_lower = True
        if 'A' <= ch <= 'Z':
            has_upper = True

        j = 0
        while j < 10:
            if ch == special_chars[j]:
                has_special = True
                break
            j += 1
        if ch == prev_char:
            repeat_count += 1
            if repeat_count > 2:
                return False
        else:
            repeat_count = 1

        prev_char = ch
        i += 1

    return has_upper and has_lower and has_digit and has_special
