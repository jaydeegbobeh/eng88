# Python Data Collection

- Lists
- Dictionaries
- Tuples
- Sets

## What are Data collections?

### Lists

##### Syntax []
CRUD Create Read Update Delete

###Lists are MUTABLE
```
shopping_list = ["juice", "strawberries", "yogurt", "chicken", "raspberries", "butter"]

print(shopping_list)
print(type(shopping_list))

print(shopping_list[2])
print(shopping_list[4])

#if we needed to replace something from the list

shopping_list[5] = "oats"

# to add something to the list use .append()
shopping_list.append("mangoes")
print(shopping_list)

# to remove something from the list use .remove()
shopping_list.remove("oats")
print(shopping_list)

# to remove last item from the list use .pop() (unless index is specified)
shopping_list.pop() 
print(shopping_list)
```
### Tuples
#### Tuples are IMMUTABLE - use for fixed data (essentials)
#### Syntax ()
use cases

```
essentials = ("eggs", "milk", "bread")
print(essentials)
print(type(essentials)) #return tuple

essentials[2] = "yogurt"
print(essentials)  #return error tuples are IMMUTABLE
```

## Dictionaries

### What are dictionaries?
#### Dictionaries are structures as KEY = VALUE
VALUE = str, int, list
#### Syntax {}

```
student_1 = {
    "name": "Jaydee",
    "key": "value",
    "stream" : "Cyber Security", #str
    "completed_lessons": "3",  #int
    "completed_lessons_names": ["variables", "operators", "data collections"] #list

}

print(student_1)
print(student_1["name"])  # fetch value with key
print(student_1["stream"])
print(student_1["completed_lessons_names"])
#display only OPERATORS from the list inside dictionary
print(student_1["completed_lessons_names"][1])

print(student_1.keys())
print(student_1.values())
```
## Sets
### Sets are data collection, but the difference is that they are unordered
#### Syntax name = {}
```
car_parts = {"wheels", "doors", "engine"}
print(car_parts)
```

#### can we add any new parts
```
car_parts.add("windows")
print(car_parts)
```

#### can we remove the item?
```
car_parts.discard("doors")
print(car_parts)
```

#### Frozen sets
##### Syntax ([])
```
frozen_set = ([1,3,5,6])
print(frozen_set)
```