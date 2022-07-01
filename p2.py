#!/bin/bash

# this lesson is about varibles and strings

print (" Welcome to Hogan's Cofee!!!!!!!!")

#input function
# varible is the answer to the input
user = input(" What is your name ?\n")

#print(user)
#pass input to print string
print ( "Hello " + user + ", thank you so much for coming in today!!\n")

#menu
menu = " Black Cofee, Espresso, Latte, Cappucino"

print( user + " what would you like to order from our menu ?\n Here is what we are serving.\n" + menu)

order  = input()

print("Sounds good " + user + ", we will have your " + order + " ready in a few minutes ! \n")
