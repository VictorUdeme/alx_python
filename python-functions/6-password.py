def validate_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for uppercase, lowercase, and digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    # Check for spaces
    if ' ' in password:
        return False

    # Check all conditions
    if has_uppercase and has_lowercase and has_digit:
        return True
    else:
        return False

# Test cases
print(validate_password("Password123"))   
print(validate_password("abc123"))        
print(validate_password("Password 123"))  
print(validate_password("password123"))  
