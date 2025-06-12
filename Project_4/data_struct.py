inventory = {}

exit = 0

print("Welcome to the Inventory Manager!")
while exit == 0:
    total_val = 0
    print("Current Inventory:")
    for item_info in inventory:
        total_val += inventory[item_info][1]
        print(f"Item: {item_info}, Quantity: {inventory[item_info][0]}, Price: ${inventory[item_info][1]}")

    print(f"Total value of inventory: ${total_val}")
    try:
        mode = int(input("Add (1), Remove (2), Update (3), or Exit (4)?: "))
    except:
        print("Not a registered mode. Try again.")
        continue
    match mode:
        case 1:
            try:
                item = input("Item?: ")
                quantity = int(input("Quantity?: "))
                price = float(input("Price?: "))
                inventory[item] = (quantity, price)
            except:
                print("Incorrect format. Try again.")
                continue
        case 2:
            try:
                item_rem = input("Remove which item?: ")
                inventory.pop(item_rem)
            except:
                print("Not a registered item. Try again.")
                continue
        case 3:
            try:
                item_update = input("Update which item?: ")
                quan_update = int(input("Quantity?: "))
                price_update = float(input("Price?: "))
                inventory[item_update] = (quan_update, price_update)
            except:
                print("Incorrect format or non-existent item. Try again.")
                continue
        case 4:
            exit = 1
        case _:
            print("Not a registered mode. Try again.")