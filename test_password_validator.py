from password_validator2 import validate_password

def test_valid_passwords():
    assert validate_password("StrongPass1!")
    assert validate_password("Aa1!aaba")  # no repetition

def test_length_constraints():
    assert not validate_password("A1b!")  # too short
    assert not validate_password("A1b!ccccccccccccccccc!")  # too long

def test_missing_requirements():
    assert not validate_password("abcdefg1!")  # no uppercase
    assert not validate_password("ABCDEFG1!")  # no lowercase
    assert not validate_password("Abcdefgh!")  # no digit
    assert not validate_password("Abcdefg1")   # no special char

def test_invalid_characters():
    assert not validate_password("Abc1234<")
    assert not validate_password("Abc1234{")
    assert not validate_password("Abc 1234!")

def test_repeating_characters():
    assert not validate_password("AAAabc123!")
    assert not validate_password("abc!!!123A")  
    assert not validate_password("Aa1!aaaa")   
    assert not validate_password("Aa1!aaaaaaaaaaaaaaaa")

def test_edge_lengths():
    assert not validate_password("Aa1!aaab")    
    assert not validate_password("Aa1!" + "a" * 15)

def test_non_string_inputs():
    assert not validate_password(12345678)
    assert not validate_password(None)
    assert not validate_password(["Abc123!"])
