from operator import truediv


if __name__ == "__main__":
    the_menu="""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **                                  **
    ** To quit at any time, type "quit" **
    **************************************
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    ***********************************
    ** What would you like to order? **
    ***********************************
    """
    print(the_menu)
    
    menu={"Wings": 0, "Cookies": 0, "Spring Rolls": 0, "Salmon": 0, "Steak": 0, "Meat Tornado": 0, "A Literal Garden": 0, "Ice Cream": 0, "Cake": 0, "Pie": 0, "Coffee": 0, "Tea": 0, "Unicorn Tears": 0}
    
while True :
    order = input(" > ").title()
    if order == "Quit".title():
        break

    if order in menu:
        menu[order] += 1
        if menu[order] == 1:
             print(f"{menu[order]} order of {order} added for you")
        else:
            print(f"{menu[order]} of {order} added for you")
    else:
         print(f"{order} is not in the menu")

print("Thanks for visit us your order is:")
for x in menu:
    if menu[x] > 0:
        print(f"{menu[x]} {x}")