def sum_num(num1, num2):
    
    name = input("What is your name?: ")
    return name, num1 + num2

def greet_user():
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    name, sum = sum_num(num1, num2)

    print(f"Hello, {name}! Welcome abroad. The sum of {num1} and {num2} is {sum}.")

greet_user()