from sys import argv
import webbrowser
import re
import urllib2

argc = 2

def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout = 1)
        return True
    except urllib2.URLError as err:
        return False

def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url


def WebLauncher(path):
    print('path', path)
    with open(path) as fp:
        for line in fp:
            print(line)
            url = Find(line)
            print(url)
            for str in url:
                webbrowser.open(str, new = 2)

def main():
    if len(argv) != argc:
        print('Argument length must be ', argc)
        exit()

    try:
        connected = is_connected()
        if connected:
            WebLauncher(argv[1])
        else:
            print('Unble to connect to internet')
    except Exception as e:
        print('ERROR: Eception occurred : ', e)

if __name__ == '__main__':
    main()
