#!bin/bash
#THIS LESSON WILL BE ABOUT PYTHON LISTS


#Normal List
from operator import ne


camping_list="tent, spoon, fork, sleepingbag, water, pans, flashlight \n"

#print(type(camping_list))
#print(camping_list)

#Python List
camping_list= ["tent", "spoon", "fork", "sleepingbag", "water", "pans", "flashlight"]
#print(type(camping_list))

#lists can have all the varibles together.
camp_site = ["Crystal Lake", 404 ,89.3,True]

# print from list
# printing from list starts from 0. 
# lists stay in sequence.
# indexing is when you grab a item on the list.

# I am bringing the tent
me = camping_list[0]
# chuck is bringing the sleepingbag
chuck = camping_list[3]

print(camping_list)
print(" I am bringing " + me)
print(" Chuck is bringing " + chuck + "\n\n")

# neative index
# listing items from right to left.

negative = camping_list[-2]

print(camping_list)

print(" This is the second from right indexed item in the camping list \n\n" + negative)

