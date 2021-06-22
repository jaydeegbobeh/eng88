# Sets are data collection, but the difference is that they are unordered
# Syntax name = {}

car_parts = {"wheels", "doors", "engine"}
print(car_parts)

#can we add any new parts
car_parts.add("windows")
print(car_parts)

#can we remove the item?
car_parts.discard("doors")
print(car_parts)

# Frozen sets
# Syntax ([])

frozen_set = ([1,3,5,6])
print(frozen_set)
