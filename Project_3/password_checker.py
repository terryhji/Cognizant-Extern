def check_pass(user_input):
    
    checks = {" one uppercase letter": 0,
              " one lowercase letter": 0,
              " one digit": 0,
              " one special character": 0,
              " 8 characters": 0}

    for c in user_input:
        if c.isupper():
            checks[" one uppercase letter"] = 1
        elif c.islower():
            checks[" one lowercase letter"] = 1
        elif c.isdigit():
            checks[" one digit"] = 1
        else:
            checks[" one special character"] = 1

    if len(user_input) >= 8:
        checks[" 8 characters"] = 1

    print_prompt = "Your password needs at least"

    count = 0

    for e in checks:
        if checks[e] == 0:
            if count == 0:
                print_prompt += e
                count += 1
            else:
                print_prompt += " and" + e
    
    if len(print_prompt) < 30:
        return "Your password is strong! 💪"
    else:
        return print_prompt + "."
    
user_input = input("Input password: ")

print(check_pass(user_input))