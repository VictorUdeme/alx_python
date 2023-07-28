def validate_password(password):
   
    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for x in password:
        if x.isupper():
            has_uppercase = True
        elif x.islower():
            has_lowercase = True
        elif x.isdigit():
            has_digit = True 
    if ' ' in password:
        return False
    
    if has_uppercase and has_lowercase and has_digit:
        return True
    else:
        return False


print(validate_password("Password123"))   
print(validate_password("abc123"))        
print(validate_password("Password 123"))  
print(validate_password("password123"))   
