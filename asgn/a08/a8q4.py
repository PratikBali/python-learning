import threading

def small(cat):
    print('id : {} name : {}'.format(threading.currentThread().ident, threading.currentThread().name))
    sum = 0
    for i in cat:
        if i.islower():
            sum = sum + 1
    print('lowercase letters are: ', sum)

def capital(cat):
    print('id : {} name : {}'.format(threading.currentThread().ident, threading.currentThread().name))
    sum = 0
    for i in cat:
        if i.isupper():
            sum = sum + 1
    print('uppercase letters are: ', sum)

def digit(cat):
    print('id : {} name : {}'.format(threading.currentThread().ident, threading.currentThread().name))
    sum = 0
    for i in cat:
        if i.isdigit():
            sum = sum + 1
    print('digits are: ', sum)


if __name__ == '__main__':
    pat = 'fvbsjdbjYTTYDXDWC*88477867'
    small = threading.Thread(target=small, args=(pat,))
    capital = threading.Thread(target=capital, args=(pat,))
    digit = threading.Thread(target=digit, args=(pat,))

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()

