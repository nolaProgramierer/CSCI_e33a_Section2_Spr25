import datetime
from datetime import date

# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
# tempor incididunt ut labore et dolore magna aliqua. Habitant morbi tristique
# senectus et. Felis eget velit aliquet sagittis id consectetur.

def some_function():
    print("Hi there!")

def foo(a, b, c):
    x = a ** c
    y = b ** c
    if x + y > 400:
        print("It's greater than 400!")
    elif x + y < 400:
        print("It's less than 400")
    else:
        print("It's 400")

foo(3, 2, 2)

def bar(x, y):
    return x + y

def another_func():
    pass

# "==" is an python equality operator
# "is" is an identity operator, 'baz' and 'None' are the same object in memory
baz = foo
if baz is None:
    pass

x = 1  # Ensure x is defined before using it
# Python allows this, but PEP 8 recommends breaking statements across lines
if x == 1:
    print("x is 1")

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 2001}
my_dict['key1'] = my_dict.get('hello', 'default_value')  # Avoid KeyError

# The function add_item has a mutable default 
# argument (lst=[]), which can lead to unexpected behavior. 
def add_item(item, lst=None):  
    if lst is None:  
        lst = []  
    lst.append(item)  
    return lst  
