def check_num(num):
    if num == 0:
        print("Zero it is. A perfect balance!")
    elif num > 0:
        print("This number is positive. Awesome!")
    else:
        print("This number is negative. Better luck next time!")

print(f"Check Number:")
num = input()
check_num(int(num))