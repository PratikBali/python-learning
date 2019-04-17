from sys import argv

argc = 2

def fun():
    print('argv[0]:', argv[0], 'argv[1]', argv[1])

def main():
    if len(argv) != argc:
        print('Argument length must be ', argc)
    else:
        if (argv[1]).isdigit():
            fun()
        else:
            print('Argument is not a number', argv[1])

if __name__ == '__main__':
    main()
