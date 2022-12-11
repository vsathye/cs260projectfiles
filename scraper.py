import requests
from bs4 import BeautifulSoup
import urllib.request

print('Search Param: ')
searchparam = input()
searchparam.replace(" ", "+")
URL = 'https://www.google.com/search?q=' + searchparam + '&sxsrf=ALeKk03xBalIZi7BAzyIRw8R4_KrIEYONg:1620885765119&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjv44CC_sXwAhUZyjgGHSgdAQ8Q_AUoAXoECAEQAw&cshid=1620885828054361'
page = requests.get(URL)

sp = BeautifulSoup(page.content, 'html.parser')
print(sp.prettify())
imgTags = sp.find_all('img', class_='yWs4tf')[:5]

links = []
for i in imgTags:
    links.append(i['src'])

l = 0
while l < 5:
	urllib.request.urlretrieve(links[l], "/Users/akarnik/Desktop/scrapedImages/image" + str(l) + ".jpg")
	l+=1