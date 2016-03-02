'''
We're going to demonstrate how to get around errors in python.
Use try: and
    except error:

We're domonstrating this method by the ZeroDivisionError, whereby the computer
cannot divide by zero... obv
'''


def divide(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print "Error: You tried to divide by zero."


nums=[1,2,12,0,5,6]

for i in range(0, len(nums)):
    print divide(nums[i])

'''
after running the program, the except clause
appears and the program continues to run normally
'''
