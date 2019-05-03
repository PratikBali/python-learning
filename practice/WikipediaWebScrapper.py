import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
print(type(res))
print(res.text)

soup = bs4.BeautifulSoup(res.text,'lxml')
print(type(soup))

title = soup.select('title')
print(title[0].getText())

print('This is ')
print(title[0].getText())

arr = soup.select('.mw-headline')

for element in arr:
    print(element.text)
