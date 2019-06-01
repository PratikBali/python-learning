from sys import argv
import os
import hashlib

argc = 2

def FindChecksum(path, block = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buffer = fd.read(block)

    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = fd.read(block)

    fd.close()
    return hasher.hexdigest()


def DirectoryCheckSum(path):

    if not os.path.isabs(path):
        cwd = os.path.abspath(path)
        print('your provided direcory', cwd)

    try:
        if os.path.isdir(path):
            files = os.listdir(cwd)

            if len(files) == 0:
                print('No files in direcory', cwd)
            else:
                for file in files:
                    file_path = os.path.join(cwd, file)
                    if (os.path.isfile(file_path)):
                        checksum = FindChecksum(file_path)
                        print(file_path, checksum)
        else:
            print('Not a direcory', cwd)
            exit()


    except OSError as e:
        print(e)
        exit()


def main():
    if len(argv) != argc:
        print('Argument length must be ', argc)
        exit()

    try:
        DirectoryCheckSum(argv[1])
    except Exception as e:
        print('ERROR: Eception occurred : ', e)

if __name__ == '__main__':
    main()
