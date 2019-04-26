from sys import argv

argc = 2

def fun(arg):
    print(arg)

def main():
    if len(argv) != argc:
        print('Argument length must be ', argc)
        exit()

    try:
        fun(argv[1])
    except Exception as e:
        print('ERROR: Eception occurred : ', e)

if __name__ == '__main__':
    main()
