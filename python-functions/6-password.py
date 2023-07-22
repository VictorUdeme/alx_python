def validate_password(password):
  """
  Validates a password.

  Args:
    password: The password to validate.

  Returns:
    True if the password passes all the checks, and False otherwise.
  """

  if len(password) < 8:
    return False

  uppercase_letters = 0
  lowercase_letters = 0
  digits = 0
  for character in password:
    if character.isupper():
      uppercase_letters += 1
    elif character.islower():
      lowercase_letters += 1
    elif character.isdigit():
      digits += 1

  if uppercase_letters == 0 or lowercase_letters == 0 or digits == 0:
    return False

  if " " in password:
    return False

  return True

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))