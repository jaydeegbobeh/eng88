# creating snake class as a child class of reptile

from reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.forked_tongue = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        return "I can smell the taste :) "

# snake_object = Snake()
# print(snake_object.use_tongue_to_smell()) # method from Snake class
# print(snake_object.seek_heat()) # method from Reptile class
# print(snake_object.venom()) # method from Animal class
