from snake import Snake


class Python(Snake):
    def __init__(self):

        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "yum yum yum"

    def climb(self):
        return "up we go"

    def shed_skin(self):
        return "Time to refresh"

python_object = Python()
dog_object = Python()
print(dog_object.eat())

print(python_object.climb()) # method from Python class
print(python_object.use_tongue_to_smell()) # method from Snake class
