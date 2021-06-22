from OOP_task_1 import SimpleCalc

class FunctionalCalc(SimpleCalc):
    def __init__(self):
        super().__init__()

    def cm_inch(self, x):
        return x * 2.54

    def div_by(self, x, y):
        if y == 0:
            return False
        elif x % y == 0:
            return True
        else:
            return False

calc_input = FunctionalCalc()

# fun_calc = FunctionalCalc()

# print("1. Addition x + y")
# print("2. Subtraction x - y")
# print("3. Division x / y")
# print("4. Multiplication x * y")
# print("5. Convert cm to inches")
# print("6 Check if x is divisible by y")
#
# choice = int(input("Please select calculator function (1-6)\n"))
# x = int(input("Enter x\n"))
# y = int(input("Enter y\n"))
#
# if choice == 1:
#     print(fun_calc.add(x, y))
# elif choice == 2:
#     print(fun_calc.subtract(x, y))
# elif choice == 3:
#     print(fun_calc.divide(x, y))
# elif choice == 4:
#     print(fun_calc.multiply(x, y))
# elif choice == 5:
#     print(fun_calc.cm_inch(x))
# elif choice == 6:
#     print(fun_calc.div_by(x, y))


# create a function for cm to inch
# create a function for divisible by , check if the number is divisible by 0 return True else False

# print statements for all the functions available in parent and child class