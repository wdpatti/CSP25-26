def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    else:
        d = False
        u = False
        for i in password:
            if i.isdigit():
                d = True
            elif i.isupper():
                u = True

        if d and u:
            return "Strong"
        elif d:
            return "Medium"
        elif not d:
            return "Weak"
        
print(check_password_strength("Pass123!"))