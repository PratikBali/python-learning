import os
import psutil

def ProcMon():
    print('hi')

    listProcess = []

    for proc in psutil.process_iter():
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        listProcess.append(pinfo)

    for proc in listProcess:
        print(proc)


def main():
    try:
        ProcMon()
    except Exception as err:
        print('HYDRA-ERROR:'err)

if __name__ == '__main__':
    main()