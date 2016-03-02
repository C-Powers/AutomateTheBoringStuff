#we're looking at dictionary data types.
#Here's an example.
#written in the form 'key':'value', 'key2':'value2', etc...

myCat={'size':'fat', 'color':'gray', 'disposition':'loud'}

#can get the value for size,color, or dispositoon by calling:

myCat['size'] #etc.

#we can also check if a key is in the dictionary by calling
'size' in myCat #which would return True

#now, we can check what keys and values we have in our list.

myCat.keys()  #returns the keys
myCat.values()  #returns the values
myCat.items() #retusn both the keys and values in a multidimensional array



for i,j in myCat.items():
    print i,j


#it's tedious to get values from dictionaries with lots of for loops,
#so we can use the .get() function.

myCat.get('size',0) #this works around a KeyError message.

#this will return to me the size of the cat, which should be 'fat'.
#if the 'size' key does not exist, I will instead get 0.


#now, if we want to add something to our dictionary, we can do it like so:

eggs = {'name':'Zophie', 'species':'cat', 'age':8}


if 'color' not in eggs:
    eggs['color']='black'

#because there was no 'color' key, there now is a 'color' key with the
#value 'black'

#we can also do this and make sure a key exist with .setdefault()

#so,
eggs.setdefault('color', 'orange')

#will return 'black' because they key already exists












#we're going to move on to more complicated dictionary mumbo jumbo.
#look at ticTacToe.py for an example of how to use them.



#dictionaries within dictionaries

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought=0
    for n,m in guests.items():
        numBrought = numBrought + m.get(item,0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
