age = int (input("How old are you? ")) # User input for age

if age >= 18: # If age is 18 or above
    print("Congratulations! You are eligible to vote. Go make a difference!")
else: # If age is below 18
    print(f"Oops! You’re not eligible yet. But hey, only {18 - age} more years to go!") # Print the difference from 18 and user age
