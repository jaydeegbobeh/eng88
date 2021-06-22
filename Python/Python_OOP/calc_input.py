from functional_calc import FunctionalCalc


class CalcInput(FunctionalCalc):
    def __init__(self):
        super().__init__()

    def user_input(self):


        print("1. Addition x + y")
        print("2. Subtraction x - y")
        print("3. Division x / y")
        print("4. Multiplication x * y")
        print("5. Convert cm to inches")
        print("6 Check if x is divisible by y")

        choice = int(input("Please select calculator function (1-6)\n"))
        x = int(input("Enter x\n"))
        y = int(input("Enter y\n"))
        start_calc = True
        while start_calc:
            if choice == 1:
                print(calc_inp.add(x, y))
            elif choice == 2:
                print(calc_inp.subtract(x, y))
            elif choice == 3:
                print(calc_inp.divide(x, y))
            elif choice == 4:
                print(calc_inp.multiply(x, y))
            elif choice == 5:
                print(calc_inp.cm_inch(x))
            elif choice == 6:
                print(calc_inp.div_by(x, y))

calc_inp = CalcInput()
calc_inp.user_input()