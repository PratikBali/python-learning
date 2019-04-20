import os
import hashlib
from sys import *
import time

argc = 2

def Checksum(path, block = 1024):
    hasher = hashlib.md5()
    fd = open(path, 'rb')
    buffer = fd.read(block)

    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = fd.read(block)
    return hasher.hexdigest()

def DuplicateDetector(path):

    if not os.path.isabs(path):
        srcdir = os.path.abspath(path)
    else:
        srcdir = path

    if not os.path.isdir(srcdir):
        print('No such a directory', srcdir)
        exit()
    else:
        duplicate_files = {}

        for dirname,sub_dir_list,files_list in os.walk(srcdir):
            for file in files_list:
                file_path = os.path.join(dirname, file)
                file_checksum = Checksum(file_path)

                if file_checksum in duplicate_files:
                    duplicate_files[file_checksum].append(file_path)
                else:
                    duplicate_files[file_checksum] = [file_path]
        return duplicate_files

def DeleteDuplicate(duplicate_files):
    print('print dup')
    results = list(filter(lambda x : len(x) > 1, duplicate_files.values()))
    if len(results) > 0:

        icnt = 0
        print('Duplicate files Found')
        for duplicate in results:
            for dup in duplicate:
                icnt += 1
                if icnt >= 2:
                    print('\t\t%s' % dup)
                    os.remove(dup)
            icnt = 0
    else:
        print('No Duplicate files Found')


def main():
    if not len(argv) == argc:
        print('Arguements length should be 2')
        exit()

    else:
        try:
            duplicate_files = DuplicateDetector(argv[1])
            DeleteDuplicate(duplicate_files)
        except Exception as e:
            print('Exception: ', e)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    exetime = end - start
    print('Execution time', exetime)
