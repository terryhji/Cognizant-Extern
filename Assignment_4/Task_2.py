info = {"name": "terry",
        "age": 24,
        "city": "toronto"}

info["favorite color"] = "yellow"
info["city"] = 'san jose'

print("Keys: ", end="")
for x in info:
    if x == "favorite color":
        print(x)
        break
    print(x, end=", ")

print("Values: ", end="")

for x in info:
    if x == "favorite color":
        print(info[x])
        break
    print(info[x], end=", ")