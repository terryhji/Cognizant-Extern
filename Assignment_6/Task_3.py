try:
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    res = num1 / num2
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    print(f"The result is {res}.")
finally:
    print("This block always executes.")
