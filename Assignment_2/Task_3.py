num = int(input("Enter a number: "))

factorial_calc = 1

for x in range(1, num + 1):
    factorial_calc *= x

print(f"The factorial of {num} is {factorial_calc}.")