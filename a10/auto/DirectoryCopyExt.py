from sys import argv
from distutils.dir_util import copy_tree
import os
import shutil

argc = 4

def fun(src, dest, ext):

    if not os.path.isabs(src):
        srcdir = os.path.abspath(src)

    destdir = os.getcwd() + '/' + dest

    try:
        if os.path.isdir(srcdir):
            src_files = os.listdir(srcdir)
        else:
            print(srcdir, ' is not a directory')
            exit()

        if not os.path.isdir(destdir):
            os.mkdir(destdir)

        if len(src_files) == 0:
            print(srcdir, ' not contains any file')
            exit()
        else:
            for file in src_files:
                file_path = os.path.join(srcdir, file)
                if (os.path.isfile(file_path)):
                    if file_path.endswith(ext):
                    # if file.endswith(ext):
                        shutil.copy(file_path, destdir)

    except OSError as e:
        print(e)
        exit()


def main():
    if len(argv) != argc:
        print('Argument length must be ', argc)
        exit()

    try:
        fun(argv[1], argv[2], argv[3])
    except Exception as e:
        print('ERROR: Eception occurred : ', e)

if __name__ == '__main__':
    main()
