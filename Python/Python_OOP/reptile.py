# creating a reptile class to Inherit everything from Animal class

from animal import Animal #example of inheritance

class Reptile(Animal):

    def __init__(self):
    #we have a key word called super which inherits everthing from parent class at the time of initialisation of this class
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]

    def seek_heat(self):
        return "it's rainy and windy, where is the sun?"

    def hunt(self):
        return "keep hunting for food until you get it"

    def use_venom(self):
        return "if I've got it I'm using it"


# create an object of Reptile class
# reptile_object = Reptile()
# print(reptile_object.hunt()) # this function is from Reptile class
# print(reptile_object.eat()) # this function is inherited from Animal parent class
