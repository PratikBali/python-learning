import os
import time
import psutil
from sys import argv

argc = 2

def ProcMonLog(srcdir):
    listProcess = []

    if not os.path.isdir(srcdir):
        print('No such a directory ', srcdir)
        print('Creating a directory : %s'%srcdir)

        try:
            os.mkdir(srcdir)
        except Exception as err:
            print('ERROR: ', err)

    if os.path.isdir(srcdir):
        separator = '-' * 80
        log_path = os.path.join(srcdir, 'ProcessLog %s.log'%(time.strftime("%a %d-%m-%Y %H-%M-%S")))
        fd = open(log_path, 'w')
        fd.write(separator + '\n')
        fd.write('Process Log %s' %(time.ctime()) + '\n')
        fd.write(separator + '\n')

        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
                listProcess.append(pinfo)
            except Exception as err:
                print('ERROR: ', err)


        for element in listProcess:
            fd.write('%s \n' % element)


def main():
    if len(argv) == 2:
        ProcMonLog(argv[1])
    else:
        print('HYDRA-ERROR: Aguements length did not match')
        exit()


if __name__ == '__main__':
    main()