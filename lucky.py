# a mini program that gives the top google result

import requests, sys, webbrowser, bs4

print("Googling...") #let the user know that the process is occuring
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#retrieve top result
soup = bs4.BeautifulSoup(res.text)

#open a bowser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
