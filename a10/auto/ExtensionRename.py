from sys import argv
import os

argc = 3

def fun(find, replace):
    # print('file: {}, prev ext: {}, new ext: {} '.format(argv[1], find, replace))
    # o = dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.getcwd()
    # print('{}, {}'.format(o,path))

    for dir,subdir,files in os.walk(path):
        for file in files:
            if not os.path.isfile(file): continue
            if file.endswith(find):
                # print(file)
                pre, ext = os.path.splitext(file)
                # print('{}  {}'.format(pre, ext))
                os.rename(file, pre + replace)
                # file.replace(find, replace)

def main():
    if len(argv) != argc:
        print('Argument length must be ', argc)
        exit()

    if (argv[1]).isdigit() or (argv[2]).isdigit():
        print('Argument should not digit ')
        exit()

    try:
        fun(argv[1], argv[2])
    except Exception as e:
        print('ERROR: Eception occurred : ', e)

if __name__ == '__main__':
    main()
