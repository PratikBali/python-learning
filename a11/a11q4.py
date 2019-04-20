import modules.DirectoryChecksum
import os

def main():
    print('execute: python DuplicateRemovalTime.py abc deleted_log_time.txt')
    os.system('python modules/DuplicateRemovalTime.py abc > deleted_log_time.txt')

if __name__ == '__main__':
    main()
