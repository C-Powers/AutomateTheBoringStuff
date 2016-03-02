'''
This code will show how a 'continue' statement operates
'''

spam=0
while spam <5:
    spam = spam+1
    if spam == 3:
        continue  #what this continue statement is going to do, is go to the start of the while loop, forgoing the print statement
    print ("spam is "+ str(spam))


'''
notice that 3 is not printed, because we skip the print statement
'''
