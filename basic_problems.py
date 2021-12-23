# -----List--------

# list how to create list
# find the length of the list
# slice of the list
# iterate list
# list modification operation(append,Replace,Remove,copy)

items_product = ["Laptop", "Mobile", "Computer", "Speakers"]  # Created List of product items
print(items_product)                    # print items_product
print(len(items_product))               # find length of the item_product
print(items_product[0:4])               # print the items from the item_product
print((items_product[:3]))              # find the first three items from the list
items_product[1] = "Headphones"          # Replace the item_product where "Mobiles"
print(items_product)
items_product[0:2] = ["TV", "Routers", "Wires"]     # Replace items_product using slice method
print(items_product)
print("Laptop" in items_product)               # Iterate items_product using in keyword
items_product.append("Cabel")                  #append new items_product
print(items_product)
items_product.remove("Speakers")       # Remove items_product from the list
print(items_product)
gadgets_items = items_product.copy()     # copied from items_products to gadgets_items
print(gadgets_items)


# ----Tuples----
numbers = (1, 3, 4, 5)  # created tuples
print(numbers)
print(numbers)          # using for loop print tuples in sequence pattern


# ----String----

Message = "hello python"         # string in python within ""
print(Message)
Message = """hello python        # string  display by using to display multiple lines
how are you"""
print(Message)
Message = "he asked,\"what\'s going on?\""  # display multiple string
print(Message)
Message = "hello python"                       # display and access String character
print(Message[0:5])

# ---Dictionary----
my_dict = {1: 'apple', 2: 'ball'}  # Create dictionary key and value
print(my_dict)  # print dictionary

my_dict = {"name": "Geeta" , ("age"): 21}  # by using key element we can access value
print(my_dict["name"])
