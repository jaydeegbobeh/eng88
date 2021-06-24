# Build a basic object oriented calculator
## 1: build a simple calculator class containing add, subtract, multiply, divide.

class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        return self.x + self.y

    def subtract(self, x, y):
        return self.x - self.y

    def multiply(self, x, y):
        return self.x * self.y

    def divide(self, x, y):
        return self.x / self.y

    def percentage(self, x, y):
        return (self.x / self.y) * 100

    def is_divisible_by(self, x, y):
        return self.x % self.y

    def triangle_area(self, x, y):
        return (self.x * self.y)/2

    def inch_to_cm(self, x):
        return self.x * 2.54

#print what calc can do before asking input
x = int(input("Enter the first number\n"))
y = int(input("Enter the second number\n"))
op = Calculator(x, y)
choice = 1

while choice != 0:
    print("Calculator operations:")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. percentage")
    print("6. is x divisible by y?")
    print("7. find the area of a triangle")
    print("8. convert inches to cm")
    print("0. exit calculator")

    choice = int(input("Enter choice:\n"))
    if choice == 1:
        print(op.add(x, y))
    elif choice == 2:
        print(op.subtract(x, y))
    elif choice == 3:
        print(op.multiply(x, y))
    elif choice == 4:
        print(op.divide(x, y))
    elif choice == 5:
        print(op.percentage(x, y), "%")
    elif choice ==6:
        if op.is_divisible_by(x,y) == 0:
            print(True)
        else:
            print(False)
    elif choice ==7:
        print(op.triangle_area(x, y))
    elif choice ==8:
        print(x, "inches is equal to", op.inch_to_cm(x), "cm")
    elif choice == 0:
        print("Bye")
    else:
        print("That's not an option, please try again")
