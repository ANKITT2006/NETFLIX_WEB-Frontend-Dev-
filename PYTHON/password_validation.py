def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    if not has_upper:
        return "Password must contain at least one uppercase letter"
    if not has_lower:
        return "Password must contain at least one lowercase letter"
    if not has_digit:
        return "Password must contain at least one digit"
    if not has_special:
        return "Password must contain at least one special character"

    return "Password is valid"


pwd = input("Enter password: ")
print(validate_password(pwd))
