import threading

def evenFactor(no):
    sum = 0
    print('Even Factor Method')
    for i in range(1, no):
        if (no % i == 0):
            if i % 2 == 0:
                sum = sum + i
    print('Even factor sum: ', sum)

def oddFactor(no):
    sum = 0
    print('Odd Factor Method')
    for i in range(1, no):
        if (no % i == 0):
            if i % 2 != 0:
                sum = sum + i
    print('Odd factor sum: ', sum)

if __name__ == "__main__":

    number = int(input('Enter Number: '))
    EvenThread = threading.Thread(target=evenFactor, args=(number,))
    OddThread = threading.Thread(target=oddFactor, args=(number,))

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()
    print('Maint thread exit')

