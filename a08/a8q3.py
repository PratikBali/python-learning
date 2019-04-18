import threading

def evenList(arr):
    sum = 0
    print('Even List Method')
    for i in arr:
        if i % 2 == 0:
            sum = sum + i
    print('Even List sum: ', sum)

def oddList(arr):
    sum = 0
    print('Odd List Method')
    for i in arr:
        if i % 2 != 0:
            sum = sum + i
    print('Odd List sum: ', sum)

if __name__ == "__main__":

    arr = [4, 35, 36, 77, 68, 25, 89, 23, 86, 93, 45, 70]

    EvenThread = threading.Thread(target=evenList, args=(arr,))
    OddThread = threading.Thread(target=oddList, args=(arr,))

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()
    print('Maint thread exit')

