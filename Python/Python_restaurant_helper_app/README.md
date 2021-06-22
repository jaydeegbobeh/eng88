# Restaurant Waiter Helper Program

### User Stories:
1. As a user I want to be able to see the menu in a formatted way, so that I can order my meal.
2. As a user I want to be able to order 3 times, and have my responses added to a list, so they aren't forgotten.
3. As a user, I want to have my order read back to me in a formatted way, so I know what I ordered.

### Acceptance Criteria:

- Implement OOP with the most suitable pillars as per your understanding
- New repo and new project
- Git tracked
- Minimum of 5 commits
- Has documentation
- Follows best practices

#### User story 1
Here I created the class Menu, with the methods starters, main_course, dessert - see menu.py.
```
class Menu:

    def starters(self):
        return "Starter:\nGuacamole with tortilla chips (VE) - £5.50\nVeggie nachos (V) - £5.95\nChorizo nachos - £6.95"

    def main_course(self):
        return "Main:\nSweet potato & feta taquito (V) - £5.95\nGrilled chicken club quesadilla - £6.95\nChargrilled steak & cheese taco - £7.95\nRainbow salad bowl (V) - £9.25"

    def dessert(self):
        return "Dessert:\nChurros (V) - £5.95\nChocolate & pecan brownie (V) - £5.95\nBlack coconut & vanilla ice cream (V) - £6.25"
```

#### User story 2
- The class Menu (parent class) is **inherited** in the UserOrder class (child class).
- The method order_input first prints the menu for the user to view and then allows the user to input their choice for starter, main and dessert.
- An object instance pls_order was created, it can be used in the order_input where all the attributes of the class Menu can be used.
- The list input_list[] stores the user's order

```
from menu import Menu


class UserOrder(Menu):

    def __init__(self):
        super().__init__()

    def order_input(self):
        print("Welcome, please take some time to look over the menu.")
        print(pls_order.starters(), "\n")
        print(pls_order.main_course(), "\n")
        print(pls_order.dessert(), "\n")
        start_choice = input("What would you like as your starter?\n")
        main_choice = input("What would you like as your main?\n")
        dess_choice = input("What would you like as you dessert?\n")

        input_list = [start_choice, main_choice, dess_choice]
        print("Here's your order:\n" + "\n".join(input_list))



pls_order = UserOrder()
pls_order.order_input()
```
#### User story 3
- A print statement was added here, so the user can view their order
- The .join() method takes all items in an iterable (in this case a list) and joins them into one string.
    - A string separator must be specified "\n" separates each item with a new line
    
```
from menu import Menu


class UserOrder(Menu):

    def __init__(self):
        super().__init__()

    def order_input(self):
        print("Welcome, please take some time to look over the menu.")
        print(pls_order.starters(), "\n")
        print(pls_order.main_course(), "\n")
        print(pls_order.dessert(), "\n")
        start_choice = input("What would you like as your starter?\n")
        main_choice = input("What would you like as your main?\n")
        dess_choice = input("What would you like as you dessert?\n")

        input_list = [start_choice, main_choice, dess_choice]
        print("Here's your order:\n" + "\n".join(input_list))



pls_order = UserOrder()
pls_order.order_input()
```