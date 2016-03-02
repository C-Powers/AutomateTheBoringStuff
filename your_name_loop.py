'''
This code is going to demonstrate how a loop can continue to loop until a
a condition is met, and how we can stop the loop once that condition is met.
Also, some programming humor ;]
'''
name = ''  #first thing we do, is create an empty string
while True:   #this will make it such that our loop continues to run as True is always met
    name = raw_input("Please type 'your name': ")
    if name == 'your name':
        break

print "Thank you for typing 'your name'"

'''
so, what happens is that the code continues to run with whatever name you enter,
unless that name happens to be 'your name'
'''
