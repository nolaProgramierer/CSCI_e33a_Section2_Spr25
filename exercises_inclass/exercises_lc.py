# List comprehension

 # [expression for item in iterable (if condition)]
    # 1) expression: expresion to evaluate and append to the new list
    # 2) item: the variable representing each element in the iterable (e.g., a list, tuple, or string).
    # 3) iterable: the sequence or iterable to iterate over
    # 4) condition (optional): an expression to filter elements based on a condition.


# This is a tuple!
composers = "Beethoven", "Ravel", "Debussy", "Rachmaninoff", "Chopin", "von Weber"

def v_composers(composer_tuple):
    new_composers = []
    for composer in composer_tuple:
        # Filtering with condition
        if "v" in composer:
            new_composers.append(composer)
    print(new_composers)

v_composers(composers)

#list_comp = [expression for item in iterable (if condition == True)]

# 2) Render the above function as a list comprehension

# 3) Render the above function but return the list as upper case 
# and with the length of the name