#!bin/bash
#THIS LESSON WILL BE ABOUT PYTHON Methods





#Python List
supplies= ["tent", "spoon", "fork", "sleepingbag", "water", "pans", "flashlight"]

#lists can have all the varibles together.
camp_site = ["Crystal Lake", 404 ,89.3,True]


#use method to add item to the list.
#.append methond only allows you a to add one thing to list.
supplies.append("toilet paper")
supplies.append("bidet")

#.extend method allows multiple items to be added to list at one time.
supplies.extend(["marshmellows, green beans"])
 
 #or 

 # add a list to another list
supplies = supplies + ["gutair", "banjo"]


#add items to front of list
#(order in list,"item added")
supplies.insert(0,"notebook")

#add items to end of list
#(order in list,"item added")
supplies.insert(-2,"hat")

print(supplies)



