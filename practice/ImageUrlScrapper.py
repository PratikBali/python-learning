import os
import bs4
import requests
from sys import argv
from urllib.request import urlopen

def ImageUrlScrapper(url):
    connection = urlopen(url)
    raw_html = connection.read()
    connection.close()
    page_soup = bs4.BeautifulSoup(raw_html, 'html.parser')
    container = page_soup.findAll('div', {'class':'item-container'})
    return container

def main():
    url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=video%20card'

    listout = ImageUrlScrapper(url)

    for elements in listout:
        print(elements.a.img['data-src'])

if __name__ == '__main__':
    main()