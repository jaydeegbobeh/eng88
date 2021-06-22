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

