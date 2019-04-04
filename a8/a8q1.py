import threading

def even(no):
    counter = 1
    while no > 0:
        if counter % 2 == 0:
            print('Even: ', counter)
            no -= 1
        counter += 1

def odd(no):
    counter = 1
    while no > 0:
        if counter % 2 != 0:
            print('   Odd: ', counter)
            no -= 1
        counter += 1

if __name__ == "__main__":
    EvenThread = threading.Thread(target=even, args=(10,))
    OddThread = threading.Thread(target=odd, args=(10,))

    EvenThread.start()
    OddThread.start()

    EvenThread.join()
    OddThread.join()

