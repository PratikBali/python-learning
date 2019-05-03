import os
import bs4
import requests
from sys import argv

# need to install lxml if mac


argc = 1

def UrlDisplay(url):
    res = requests.get(url)
    print('res',type(res))

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    print('soup',type(soup))

    links = soup.find_all('a',href = True)

    return links

def main():
    if not len(argv) == argc:
        print('Argument length must be ', argc)
        exit()
    else:
        url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

    try:
        arr = UrlDisplay(url)
        # print('arr',arr)
    except Exception as e:
        print('ERROR: Eception occurred : ', e)

    print('Links are ')

    for element in arr:
        if '#' not in element['href']:
            print(element['href'])

if __name__ == '__main__':
    main()
