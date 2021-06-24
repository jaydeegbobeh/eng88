class FizzBuzz():

    def fz_bz(self):
        for i in range(1,101):
            if i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            else:
                print(i)


fizz_buzz = FizzBuzz()
fizz_buzz.fz_bz()




