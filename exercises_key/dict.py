# List of car dictionaries
cars = [
    {"brand": "BMW", "trim": "328i", "color": "gray", "price": 38900},
    {"brand": "Mercedes", "trim": "350E", "color": "white", "price": 89000},
    {"brand": "Porsche", "trim": "911", "color": "orange", "price": 95000},
    {"brand": "Kia", "trim": "Sorento", "color": "blue", "price": 30900},
    {"brand": "Toyota", "trim": "Sienna", "color": "gray", "price": 51200},
]

print("1)")
# Find orange car using 'get' method
# Using 'get' prevents a KeyError if a key:value pair doesn't exist
def find_orange_car(obj_list):
    return [car for car in obj_list if car.get("color") == "orange"]

print("Orange car:", find_orange_car(cars))


print()
print("2)")
# Find cars that are less than $40000 (list comprehension)
cheap_cars = [car for car in cars if car["price"] < 40000]
print("Cheap cars:", cheap_cars)


print()
print("3)")
# Find cars that are less than $40000 (dictionary comprehension)
cheap_cars_dict = {car["brand"]: car["price"] for car in cars if car["price"] < 40000}
print(f"Cheap cars: {cheap_cars_dict}")


print()
print("4)")
# Find the most expensive car brand
# 'max' returns the largest item in an iterable based on the values
# returned by the 'key' function
def find_expensive_car_brand(cars):
    most_expensive = max(cars, key=lambda car: car["price"])
    return most_expensive["brand"]

print(f"Most expensive car brand: {find_expensive_car_brand(cars)}")


print()
print("Dictionary examples")
#------------------------------------------------------
# Piano dictionary
pianos = {"Steinway": 85000, "Bechstein": 95000, "Steingräber": 105000, "Rönisch": 65000, "Blüthner": 92000}

# 1) List of piano brands (keys)
piano_brands = list(pianos.keys())
print(f"Piano brands: {piano_brands}")

print()
# 2) List of piano prices (values)
piano_prices = list(pianos.values())
print(f"Piano prices: {piano_prices}")

print()
# 3) List of key-value pairs
piano_items = list(pianos.items())
print(f"Piano key-value pairs: {piano_items}")

print()
# 4) Find list of pianos priced above 85,000 using list comprehension
expensive_pianos = [brand for brand, price in pianos.items() if price > 85000]
print(f"Pianos above 85,000: {expensive_pianos}")

print()
# 5) Find the most expensive piano
# Using pianos.get without parentheses is just passing a reference 
# to the get method itself, which will be invoked 
# later with each dictionary key as the argument by the max() function.
most_valuable_piano = max(pianos, key=pianos.get)
print(f"Most valuable piano: {most_valuable_piano}")

print()
# 6) List of pianos without umlauts
import re
no_umlaut_pianos = [brand for brand in pianos if not re.search("[üäö]", brand)]
print(f"Pianos without umlauts: {no_umlaut_pianos}")

    
