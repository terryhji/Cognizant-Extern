res = 0
while res == 0:
    try:
        num = float(input("Enter a number: "))
        res = 100 / num 
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

print(f"100 divided by {num} is {res}.")
