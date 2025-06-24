cond = 0
while cond == 0:
    try:
        mode = int(input("(1) Addition, (2) Subtraction, (3) Multiplication, (4) Division, (5) Exit: "))
    except:
        print("Invalid input. Try again")
        continue
    if mode > 0 and mode < 5:
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
    match mode:
        case 1:
            sum = num1 + num2
            print(f"{num1} added by {num2} is {sum}.")
        case 2:
            sum = num1 - num2
            print(f"{num1} subtracted by {num2} is {sum}.")
        case 3:
            sum = num1 * num2
            print(f"{num1} multiplied by {num2} is {sum}.")
        case 4:
            try:
                sum = num1 / num2
                print(f"{num1} divided by {num2} is {sum}.")
            except ZeroDivisionError:
                print("Oops! You cannot divide by zero.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        case 5:
            cond = 1