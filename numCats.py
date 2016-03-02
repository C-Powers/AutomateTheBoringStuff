#number of cats
#another look at try/except

numCats = raw_input("How many cats do you have? __________")
try:
    if int(numCats) >= 4 and int(numCats)>=0:
        print "That is a lot of cats."
    elif int(numCats) <0:
        print "Please stop killing cats!"
    else:
        print "That's not that many cats."
except ValueError:
    print "Please enter a number."
