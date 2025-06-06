num = int(input("Enter a number: "))

mult_string = ""

for x in range(1, 11):
    mult_string += f"{num} x {x} = {num * x} "

print(mult_string)