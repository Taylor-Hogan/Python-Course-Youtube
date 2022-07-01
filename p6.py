#!/bin/bash

# this lesson is learning if else eslif statement part 2
# this lesson is about nested IF statements

print (" Welcome to Hogan's Cofee!!!!!!!!")

#input function
# varible is the answer to the input
user = input(" What is your name ?\n")

# check what person enters the door.
# if person is an evil ben then reject. if it is anyone else then contine.
# ask if ben is evvil. IF not let him in. 
 

if user == "Ben":
    #this is a nested IF statement.if answer is Y then quit. else continue
    evil_status = input("Are you evil? (y/n)\n")
    if(evil_status == "y"):
        print("Please leave! You are not welcome here.\n")
         #use quit() or exit() to end script if statment is true
        quit()
    else: print("Great! I am glad you are not Evil " + user + "\n\n")

else:
    


#print(user)
#pass input to print string
    print( "Hello " + user + ", thank you so much for coming in today!!\n")

#menu
menu = " \n Black Cofee, Espresso, Latte, Cappucino"

#gives user a menu
print( user + " What would you like to order from our menu ?\n\n Here is what we are serving.\n" + menu)


# convert varible to int. you can not MULTIPLY  STRING AND NUMBER. YOU MUST USE CHANGE TO INT().
order  = input()
price = 0
#use if statment to decide price of menu item.
if order == "Black Cofee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    price = 10
elif order == "Cappucino":
    price = 7
else:
    print(" Sorry we do not have that here.")
    exit()

#print(price)
invetory = input(" How many would you like ? ")

# add prices to each menu item and add them.
#price = 8
total = int(invetory) * price

# CAN NOT CONCATICNATE STRING AND INT.  MUST USE TWOS STRINGS.  USE STR(VARIBLE)
print(" Your total is $" + str(total))
print("Sounds good " + user + ", we will have your " + order + " ready in a few minutes ! \n")
