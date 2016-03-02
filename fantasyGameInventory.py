#create a dictionary that can be used to inut items, and number of items
import numpy as np
import pprint
inventory={}

def createInventory(item, quantity):
    totalItems=0
    inventory[item] = quantity
    print inventory


def totalItems(inventory):
    totalItems=0
    pprint.pprint(inventory)
    totalItems=np.sum(inventory.values()) #this works because each entry is single dimensional
    print "Total Number of Items: " + str(totalItems)



# we can also do this by being able to input values
#we want to use raw_input for the item because it immediate imports it as a string
#we want to use input() because it imports as a value.
'''createInventory(raw_input("Please enter the name of the item.........."),
    input("How much of the item do you have?..........") )
'''

#now, let's add 10 items

for i in range(9):
    createInventory(raw_input("Item?.........."),
        input("Quantity?..........") )
totalItems(inventory)
