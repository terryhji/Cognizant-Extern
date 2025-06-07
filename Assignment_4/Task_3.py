fav_things = ('kendrick', 'nas', 'mfdoom')

print(f"Favorite things: {fav_things}")
try:
    fav_things[0] = 'benny'
except:
    print("Oops! Tuples cannot be changed.")

print(f"Length of tuple: {len(fav_things)}")