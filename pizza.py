#Name: Alex Janssens
#Prog Purpose: This program calculates pizza. Mmmmmmmm pizza.
#Note all fees are per credit
#Small = $9.99
#Medium = $12.99
#Large = $14.99
#X-Large = $17.99
#Sales tax = 5.5%

import datetime
#define pizza size cost and sales tax
SMALL = 9.99
MEDIUM = 12.99
LARGE = 14.99
XLARGE = 17.99
TAX = .055

#define global variables
order = 0
num_pizzas = 0
cost = 0
tax = 0
total = 0

# define program functions
def main():
    another_pizza = True
    while another_pizza:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to order more pizzas (Y/N): ")
        if yesno == "N" or yesno == "n":
            another_pizza = False
            print('Thank you, come again!')


def get_user_data():
    global order, num_pizzas
    order = str(input("What size pizza would you like?\nEnter S for small, M for medium, L for large, X for Xtra Large:  "))
    num_pizzas = int(input("How many pizzas would you like to order: "))

def perform_calculations():
    global order, num_pizzas, cost, tax, total
    if order == "S" or order == "s":
        cost = num_pizzas * SMALL
    elif order == "M" or order == "m":
        cost = num_pizzas * MEDIUM
    elif order == "L" or order == "l":
        cost = num_pizzas * LARGE
    elif order == "X" or order == "x":
        cost = num_pizzas * XLARGE

    tax = cost * TAX
    total = cost + tax

def display_results():
    print('\n------------------------------------')
    print('Number of pizzas  : ' + format(num_pizzas,'10,.0f'))
    print('Size of pizza                ' + str(order))
    print('Cost of pizza     $ ' + format(cost,'10,.2f'))
    print('Sales Tax         $ ' + format(tax,'10,.2f'))
    print('Sub Total         $ ' + format(total,'10,.2f'))
    print('--------------------------------------')
    print(str(datetime.datetime.now()))
    print('Thank you for choosing Palermo Pizza')

# Call on main program to execute


main()
