import os
import psutil
from sys import argv
argc = 2

def ProcSearch(proc_to_search):
    print('hi', proc_to_search)

    listProcess = []

    for proc in psutil.process_iter():

        pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])

        if pinfo.get('name') == proc_to_search:
            print(pinfo)


def main():
    if len(argv) == 2:
        try:
            ProcSearch(argv[1])
        except Exception as err:
            print('HYDRA-ERROR:',err)
    else:
        print('HYDRA-ERROR: Aguements length did not match')
        exit()

if __name__ == '__main__':
    main()