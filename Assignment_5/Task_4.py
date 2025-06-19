def factorial(num, sum):
    if num == 0:
        return sum
    sum *= num
    return factorial(num - 1, sum)

fib_arr = [0, 1]
def fibonacci(n, fib_arr):
    n -= 1
    if n == 0:
        return fib_arr
    fib_arr.append(fib_arr[-1] + fib_arr[-2])
    return fibonacci(n, fib_arr)

num = 5
n = 6

fib_arr = fibonacci(n, fib_arr)
print(f"Factorial of {num} is {factorial(num, 1)}. The {n}th Fibonacci number is {fib_arr[-1]}")

    
