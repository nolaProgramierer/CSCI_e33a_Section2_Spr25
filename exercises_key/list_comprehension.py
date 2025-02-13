# List comprehension

 # [expression for item in iterable (if condition)]
    # 1) expression: expresion to evaluate and append to the new list
    # 2) item: the variable representing each element in the iterable (e.g., a list, tuple, or string).
    # 3) iterable: the sequence or iterable to iterate over
    # 4) condition (optional): An expression to filter elements based on a condition.
# A function to return all composers with 'v' in the name

# tuple
composers = "Beethoven", "Ravel", "Debussy", "Rachmaninoff", "Chopin", "von Weber"

def v_composers(composer_tuple):
    new_composers = []
    for composer in composer_tuple:
        if "v" in composer:
            new_composers.append(composer)
    print(new_composers)

print("1)")
v_composers(composers)

# list_comp = [expression for item in iterable (if condition == True)]
# The return value is a new list, leaving the old list unchanged (functional programming).

# The expression is the current item in the iteration but also the outcome which can 
# be manipulated before it is added to the new list
# The condition is like a filter that only accepts the items that valuate to True.

print()
print("2)")
# 2) Render the above function as a list comprehension
new_composers0 = [composer for composer in composers if "v" in composer]
print(new_composers0)

# Expression (composer): This is the element (composer) we want to include in the new list.
# Iterable (composers): We are iterating over the tuple composers.
# Condition (if "v" in composer): Only include composers whose name contains the letter 'v'.


print()
print("3)")
# 3) Render the above function but return the list as upper case and with the length of the name
new_composers1 = [(composer.upper(), len(composer))for composer in composers if "v" in composer]
print(new_composers1)








