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
    container = page_soup.findAll('a', {'class':'a-link-normal a-text-normal'})
    return container

def main():
    url = 'https://www.amazon.in/s?k=macbook&ref=nb_sb_noss'

    listout = ImageUrlScrapper(url)

    for elements in listout:
        print(elements['href'])
        print()

if __name__ == '__main__':
    main()