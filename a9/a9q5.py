import sys

def openFile():
    try:
        fd1 = open(sys.argv[1], 'r', encoding ='utf-8')
    except IOError as io:
        print('Error in opening file or File does not exist')
    else:
        flag = True
        counter = 0
        offset = 0
        t1 = fd1.read()
        sub = 'this'

        while flag:
            if t1:
                print(t1)
                offset = t1.find(sub, offset, len(t1) -1)
                counter = counter + 1
                fd1.seek(offset + len(sub))
                t1 = fd1.read()
            else:
                flag = False

        print('frequency of this is:', counter)


        fd1.close()

openFile()