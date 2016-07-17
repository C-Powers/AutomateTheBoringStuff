import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ''.join(sys.argv[1:])
    #print(address)
else:
    #Get address from clipboard
    address = pyperclip.paste()
    print(address)

webbrowser.open('https://www.google.com/maps/place/ + address')
