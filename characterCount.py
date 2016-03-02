#characterCount.py
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {} #want: ex: 'r':12

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character]+1

pprint.pprint(count) #pprint will output in order, and in a column

textChar=pprint.pformat(count) #pformat will return a string value

print textChar #so using this we can print the same as we've already printed
