from sys import *
import os

def DirectoryWatcher(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is: "+foldername)
            for subf in subfolder:
                print("Sub folder of"+foldername+"is :"+subf)
            for filen in filname:
                print("File inside"+foldername+"is :"+filen)
            print('')
    else:
        print("Invalid path")
def main():
    print("----Welcome Automation----")

    print("Application name :"+argv[0])

    if(len(argv)!= 2):
        print("Error : Invalid number of argument")
        exit()

    if(argv[1] =="-h") or (argv[1] =="-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if(argv[1] =="-u") or (argv[1] =="-U"):
        print("usage : ApplicationName Absolutepath_of_Directory")
        exit()
    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

if __name__ == "__main__":
    main()
