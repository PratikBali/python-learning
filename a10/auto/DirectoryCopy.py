from sys import argv
from distutils.dir_util import copy_tree
import os

argc = 3

def fun(src, dest):
    # print('src:', src, 'dest', dest)

    if not os.path.isabs(src):
        srcdir = os.path.abspath(src)

    destdir = os.getcwd() + '/' + dest

    # print(destdir)
    # print(srcdir)

    copy_tree(srcdir, destdir)

    try:
        if not os.path.isdir(destdir):
            os.mkdir(destdir)
    except OSError as e:
        print(e)
        exit()


def main():
    if len(argv) != argc:
        print('Argument length must be ', argc)
        exit()

    try:
        fun(argv[1], argv[2])
    except Exception as e:
        print('ERROR: Eception occurred : ', e)

if __name__ == '__main__':
    main()
