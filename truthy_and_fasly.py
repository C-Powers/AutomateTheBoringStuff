#this code looks at truthy and falsey values.
#no boolean operators are used, but if we enter a name, it's "truthy" because
#we did input something
#if we dont input a name, it's falsey, because we did not input a name


name=raw_input("Please enter a name: ")
if name:
    print "Thank you so much for entering a name. :]"
else:
    print "you did not enter a name :["



'''
Please note that the above method is not particularly good. The best way to do it
would be by using an operator, such as !=. So, it would look like:

if name !=''

which means, that if the name input is not blank.
'''
