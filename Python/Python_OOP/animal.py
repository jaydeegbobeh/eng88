# animal file to create Animal class
# use pass when you have to create a class but don't know yet what functions, variables you would like to place inside

class Animal:

    def __init__(self): # self refers to this class
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "keep breathing to stay alive"

    def eat(self):
        return "nom nom nom"

    def move(self):
        return "moving all around the world"

# create an object of our Animal class
# cat = Animal() # create an object of our Animal class called cat
# print(cat.breathe()) # breathe for cat is abstracted
