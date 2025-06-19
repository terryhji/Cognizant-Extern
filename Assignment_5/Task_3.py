def make_sandwich(*args):
    print("Making a sandwich with the following ingredients: ", end="")
    for ing in args:
        print(f"- {ing}", end=" ")

make_sandwich('apple', 'lettuce', 'tomato')