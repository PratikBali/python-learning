import modules.DirectoryChecksum
import os

def main():
    print('execute: python DuplicateRemoval.py abc deleted_log.txt')
    os.system('python modules/DuplicateRemoval.py abc > deleted_log.txt')

if __name__ == '__main__':
    main()
