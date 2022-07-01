#!/bin/bash

# this lesson is about varibles and strings

import string


print (" Welcome to Hogan's Cofee!!!!!!!!")

#input function
# varible is the answer to the input
user = input(" What is your name ?\n")

#print(user)
#pass input to print string
print ( "Hello " + user + ", thank you so much for coming in today!!\n")

#menu
menu = " Black Cofee, Espresso, Latte, Cappucino"

#gives user a menu
print( user + " what would you like to order from our menu ?\n Here is what we are serving.\n" + menu)


# convert varible to int. you can not MULTIPLY  STRING AND NUMBER. YOU MUST USE CHANGE TO INT().
order  = input()
invetory = input(" How many would you like ? ")
price = 8
total = int(invetory) * price

# CAN NOT CONCATICNATE STRING AND INT.  MUST USE TWOS STRINGS.  USE STR(VARIBLE)
print(" Your total is $" + str(total))
print("Sounds good " + user + ", we will have your " + order + " ready in a few minutes ! \n")
