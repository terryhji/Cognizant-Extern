def factorial(num, sum): # Calculates factorial using user inputs
    if num == 0:
        return sum
    sum *= num
    return factorial(num - 1, sum)

def fibonacci(n, fib_arr): # Calculates nth fibonacci using user inputs
    n -= 1
    if n == 0:
        return fib_arr
    fib_arr.append(fib_arr[-1] + fib_arr[-2])
    return fibonacci(n, fib_arr)

def menu(): # Asks for inputs and choice between factorial or fibonacci mode
    choice = int(input("Choose an option: \n(1) Calculate factorial of a number \n(2) Find the nth Fibonacci number \n(3) Exit: "))
    if choice == 3: # Return while loop exit condition when exit mode is chosen
        return 0
    if choice == 1:
        num = int(input("Enter a number to find its factorial: "))
        while num < 0:
            print("Input number is below 0.")
            num = int(input("Enter a number to find its factorial: "))
        print(f"The factorial of {num} is {factorial(num, 1)}")
    else:
        n = int(input("Enter the position of the Fibonacci number: "))
        while n < 0:
            print("Input position is below 0.")
            num = int(input("Enter the position of the Fibonacci number: "))
        fib_arr = [0, 1]
        fib_arr = fibonacci(n, fib_arr)
        print(f"The {n}th Fibonacci number is {fib_arr[-1]}")
    return 1 # Return 1 to loop menu again

cond = 1 
while cond: # Keeps looping until exit condition
    cond = menu()






    
