# Lists
# Syntax []
#CRUD Create Read Update Delete
shopping_list = ["juice", "strawberries", "yogurt", "chicken", "raspberries", "butter"]

print(shopping_list)
print(type(shopping_list))

print(shopping_list[2])
print(shopping_list[4])

#if we needed to replace something from the list

shopping_list[5] = "oats"

# add something to the list
shopping_list.append("mangos")
print(shopping_list)

#to remove something from the list use .remove
shopping_list.remove("oats")
print(shopping_list)

shopping_list.pop() #removes last item from the list unless index is specified
print(shopping_list)
# lists can hold integers and strings

### Tuples
#### Tuples are IMMUTABLE - use for fixed data (essentials)
# Syntax ()
# use cases

essentials = ("eggs", "milk", "bread")
print(essentials)
print(type(essentials)) #return tuple

essentials[2] = "yogurt"
print(essentials)  #return error tuples are IMMUTABLE