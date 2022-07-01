#!bin/bash
#THIS LESSON WILL BE ABOUT PYTHON Methods
#This lesson will be about removing data from a list.





#Python List
supplies= ["tent", "spoon", "fork", "sleepingbag", "water", "pans", "flashlight"]

#lists can have all the varibles together.
camp_site = ["Crystal Lake", 404 ,89.3,True]


#use method to delete item to the list.
#.remove methond to remove one thing to list.
#supplies.remove("tent")

# remove sleepingbag from list
# the POP methond removes the item in the list.
#use print to tell you what you removed.
print("This item was just deleted :  " + supplies.pop(0))



#remove the next index number.
supplies.pop(3)

print(supplies)

#remove the tempature at the campsite.
print( camp_site)
print("We are removing the temp from list /n/n") 
print( camp_site.pop(2))
print( camp_site)






