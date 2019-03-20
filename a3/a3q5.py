from PrimeModule import *

arr = list()

def ListPrime():
    sumprime = 0
    n = input('How many Number do you want to enter: ')
    for i in range(0,int(n)):
        no = input('Num: ')

        prime = ChkPrime(no)

        if prime != 0 :
            arr.append(int(prime))
            sumprime = sumprime + prime

    return sumprime

ret = ListPrime()
print('Your Elements: ', arr)
print('Addition of all your prime elements are: ', ret)