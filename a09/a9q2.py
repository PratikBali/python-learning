def openFile():
    try:
        fd = open('Demo.txt', 'r', encoding ='utf-8')
    except IOError as io:
        print('File does not exist')
    else:
        print('File  exist')
        print(fd)
        t = fd.read()
        print(t)
        fd.close()

openFile()