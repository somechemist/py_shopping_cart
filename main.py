#!/usr/bin/env python3
# Written by Justin Powell
# 03/19/2022
# The concept is more of a POS (Mainly because I wanted to have a receipt for some reason) but still has the shipping aspect requested.
# When I have more time to play around, I would like to make the cart an object just to practice.
import time

total = 0

#Cashier login
print("\n"*100)
cashier = input("Which Cashier is using this machine?\n")
print("\n"*100)


# Define Product class
class Product:

    def __init__(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity


#Shipping Class
class Shipping:
    full = 4.95
    red = 2.95
    free = 0

# Populate the store
product1 = Product("Red Flower", "RF1", 32.95, 0)
product2 = Product("Green Flower", "GF1", 24.95, 0)
product3 = Product("Blue Flower", "BF1", 7.95, 0)

# Launch the Cashier welcome
offers =["Buy one, get one half off", "Reduced shipping for totals between $50-89$", "Free shipping for totals of $90 or greater"]
print(f"Welcome {cashier}!.\nHere are your active offers\n")
for x in offers:
    print(f"{x}: Active")
time.sleep(2.5)
print("\n\n\nSwitching to customer view\n")
time.sleep(1)
running = True

# Launch the customer view
while (running==True):
    print("\n"*100)
    print("Welcome to the Dev Flower Company!\nWe have the following products available\n\n\n\n")
    print("                PRODUCT            CODE    PRICE")
    print(f"Enter 1 to ADD a {product1.name}        {product1.code}     ${product1.price}")
    print(f"Enter 2 to ADD a {product2.name}      {product2.code}     ${product2.price}")
    print(f"Enter 3 to ADD a {product3.name}       {product3.code}     ${product3.price}")
    print("Enter 4 to VIEW your cart")
    print("Enter 5 to CLEAR your cart")
    print("Enter 6 to Checkout (shipping and discounts are applied here)")
    a = input("\n\nPlease make a selection\n")
    try:
        a = float(a)
        if (a == 1):
            print("\n" * 100)
            print(f"{product1.name} added to cart")
            total = total + product1.price
            product1.quantity = product1.quantity + 1
            time.sleep(0.75)
        elif (a == 2):
            print("\n" * 100)
            print(f"{product2.name} added to cart")
            total = total + product2.price
            product2.quantity = product2.quantity + 1
            time.sleep(0.75)
        elif (a == 3):
            print("\n" * 100)
            print(f"{product3.name} added to cart")
            total = total + product3.price
            product3.quantity = product3.quantity + 1
            time.sleep(0.75)
        elif (a == 4):
            print("\n" * 100)
            if (total > 0):
                total = round(total, 2)
                print("Product:         Quantity:")
                if (product1.quantity > 0):
                    print(f"{product1.name}       {product1.quantity}")
                if (product2.quantity > 0):
                    print(f"{product2.name}     {product2.quantity}")
                if (product3.quantity > 0):
                    print(f"{product3.name}      {product3.quantity}")
                print(f"Your total is currently: ${total}")
            else:
                print("Your cart is empty")
            time.sleep(3)
        elif (a == 5):
            print("\n" * 100)
            print("The cart has been cleared")
            total = 0
            product1.quantity = 0
            product2.quantity = 0
            product3.quantity = 0
            time.sleep(3)
        elif (a == 6):
            if (total > 0):
                print("\n" * 100)
                print(":::RECEIPT:::\n\n")
                print(f"Your Cashier is: {cashier}")
                print("Dev Flower Company")
                print("111 Monty Py. rd")
                print("Holy Grail, USA 99999\n\n")

                if (product1.quantity > 1):
                    print(f"Congratulations! You got a discount on {product1.name}s")
                    discount = product1.price * 0.5
                    total = total - discount - 0.005

                if (product2.quantity > 1):
                    print(f"Congratulations! You got a discount on {product2.name}s")
                    discount = product2.price * 0.5
                    total = total - discount

                if (product3.quantity > 1):
                    print(f"Congratulations! You got a discount on {product3.name}s")
                    discount = product3.price * 0.5
                    total = total - discount

                total = round(total, 2)

                if (total < 50):
                    shipping = Shipping.full
                elif (50 <= total < 90):
                    shipping = Shipping.red
                else:
                    shipping = Shipping.free

                grandTotal = total + shipping
                grandTotal = round(grandTotal, 2)

                print(f"\nCart total: ${total}")
                print(f"Shipping:   ${shipping}")
                print(f"\nTotal due:  ${grandTotal}")
                running = False
            else:
                print("\n\n\nOops!\nYou don't have any items to checkout with!")
                time.sleep(2)
        else:
            print("\n" * 100)
            ex = input("To exit, please enter 1 (all other options will resume\n")
            try:
                ex = int(ex)
                if (ex == 1):
                    running = False
                else:
                    pass;
            except ValueError:
                pass
    except ValueError:
        print("\n" * 100)
        print("\n\n\nplease only use numbers")
        time.sleep(2)
print("\n\nThank you for your business - Dev Flower Company")
