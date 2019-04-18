def openFile():
    try:
        fd = open('Demo1.txt', 'r')
    except IOError as io:
        print('File does not exist')
    else:
        print('File  exist')
        print(fd)
        fd.close()

openFile()