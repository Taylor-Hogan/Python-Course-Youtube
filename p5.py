#!/bin/bash

# this lesson is learning if else eslif statementa




print (" Welcome to Hogan's Cofee!!!!!!!!")

#input function
# varible is the answer to the input
user = input(" What is your name ?\n")

# check what person enters the door.
# if person is ben then reject. if it is anyone else then contine.
 
if user == "Ben" or user == "ben":

    print("Please leave! You are not welcome here.\n")
    #use quit() or exit() to end script if statment is true
    quit()
else:
    print("Hello " + user )


#print(user)
#pass input to print string
print( "Hello " + user + ", thank you so much for coming in today!!\n")

#menu
menu = " Black Cofee, Espresso, Latte, Cappucino"

#gives user a menu
print( user + " What would you like to order from our menu ?\n Here is what we are serving.\n" + menu)


# convert varible to int. you can not MULTIPLY  STRING AND NUMBER. YOU MUST USE CHANGE TO INT().
order  = input()
invetory = input(" How many would you like ? ")
price = 8
total = int(invetory) * price

# CAN NOT CONCATICNATE STRING AND INT.  MUST USE TWOS STRINGS.  USE STR(VARIBLE)
print(" Your total is $" + str(total))
print("Sounds good " + user + ", we will have your " + order + " ready in a few minutes ! \n")
