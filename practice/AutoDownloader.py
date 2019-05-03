import os
import requests
from sys import argv
from urllib.parse import urlparse

def is_downloadable(url):
    h = requests.head(url, allow_redirects = True)
    headers = h.headers
    content_type = headers.get('content-type')

    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False

    return True

def get_filename_from_cd(cd):
    a = urlparse(cd)
    return os.path.basename(a.path)

def Download(url):
    if is_downloadable(url):
        try:
            res = requests.get(url, allow_redirects = True)

            filename = get_filename_from_cd(url)
            fd = open(filename , 'wb')

            for buffer in res.iter_content(1024):
                fd.write(buffer)

            fd.close()
            return True

        except Exception as err:
            return False

    else:
        return False

def main():
    url = 'https://www.google.com/favicon.ico'

    result = Download(url)

    if result:
        print('Download Successfull')
    else:
        print('Download failed')

if __name__ == '__main__':
    main()

