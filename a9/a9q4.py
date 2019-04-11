import sys

def openFile():
    try:
        fd1 = open(sys.argv[1], 'r', encoding ='utf-8')
        fd2 = open(sys.argv[2],'r',encoding ='utf-8')
    except IOError as io:
        print('Error in opening file or File does not exist')
    else:
        t1 = fd1.read()
        t2 = fd2.read()

        if t1 == t2:
            print ('same')
        else:
            print ('diff')
            pass


        fd1.close()
        fd2.close()

openFile()