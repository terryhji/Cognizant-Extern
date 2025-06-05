def input(num):
    if num == 0:
        print("Zero it is. A perfect balance!")
    elif num > 0:
        print("This number is positive. Awesome!")
    else:
        print("This number is negative. Better luck next time!")

num_arr = [-1, 5, 0]
for num in num_arr:
    input(num)