from sys import argv
import os

argc = 3

def fun(path, ext):
    flag = False

    if not os.path.isabs(path):
        path = os.path.abspath(path)
        isdir = os.path.isdir(path)

    if isdir:
        print('Files with .py extension are:')

        for dir,subdir,files in os.walk(path):
            for file in files:
                if file.endswith(ext):
                    flag = True
                    print(file)

        if not flag:
            print('Sorry no Files found with {} extension!'.format(ext))


def main():
    if len(argv) != argc:
        print('Argument length must be ', argc)
    else:
        if (argv[1]).isdigit() or (argv[2]).isdigit():
            print('Argument should not a number')
        else:
            fun(argv[1], argv[2])

if __name__ == '__main__':
    main()
