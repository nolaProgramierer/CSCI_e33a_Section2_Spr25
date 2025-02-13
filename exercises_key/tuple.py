# Tuples
# A tuple is sequence of values, of any type, that are immutable
# Tuples are written with round brackets.
# Immutability, faster that lists, multiple return values, 
# protect data from modification


print("1)")
# Instantiate a tuple
t1 = ('a', 'b', 'c', 'd', 'e')
print(t1)


print()
print("2)")
# Tuples are hashable, and as such can be used as dictionary keys

location_data = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}

print(location_data[(40.7128, -74.0060)])  # Output: New York


print()
print("3)")
# Swap values without a temporary variable
a, b = 5, 10
a, b = b, a
print(a, b)


print()
print("4)")
# Tuples are useful for grouping related data, 
# such as representing a point (x, y) in 2D space.
point = (3, 4)  # A fixed (x, y) coordinate

def distance_from_origin(p):
    x, y = p
    return (x**2 + y**2) ** 0.5

print(distance_from_origin(point))  


# Packing & Unpacking

# Packing in Python generally refers to collecting multiple values 
# into a single variable, typically using tuples, lists, or 
# dictionaries. This is useful for various operations like 
# returning multiple values from a function or passing a 
# variable number of arguments to a function.
print()
print("5)")
# Packing position arguments
def display_piano_details(brand, finish, price):
    print(f"Brand: {brand}, Finish: {finish}, Price: ${price}")

# Packing a tuple
piano_details = ("Yamaha", "Glossy Black", 3500)

# Unpacking the tuple into function arguments
display_piano_details(*piano_details)

# Equivalent to the following:
# Keyword arugments
display_piano_details(brand="Yamaha", finish="Glossy Black", price=3500)
# Positional arguments (same order as the function parameters)
display_piano_details("Yamaha", "Glossy Black", 3500)


print()
print("6)")
# Packing keyword arguments
def display_piano_details(brand, finish, price):
    print(f"Brand: {brand}, Finish: {finish}, Price: ${price}")

# Packing a dictionary
piano_details = {"brand": "Yamaha", "finish": "Glossy Black", "price": 3500}

# Unpacking the dictionary into function arguments
display_piano_details(**piano_details)

# Equivalent to the following:
# Keyword arugments
display_piano_details(brand="Yamaha", finish="Glossy Black", price=3500)


print()
print("7)")
#Sum a tuple
t3 = (1, 2, 3, 4)
print(sum(t3))

  