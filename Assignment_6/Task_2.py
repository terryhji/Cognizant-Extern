# Index error, trying to access index 2 when only index 0 and 1 exists
try:
    arr = [1, 2]
    print(arr[2])
except IndexError:
    print("IndexError occurred! List index out of range.")
# Key error, trying to access key 3 when it does not exist
try:
    tmp_dict = {1: 0, 2: 0}
    print(tmp_dict[3])
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")
# Type error, adding string "1" and int 1 together which does not work
try:
    print("1" + 1)
except TypeError:
    print("TypeError occurred! Unsupported operand types.")