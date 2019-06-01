arr = list()


def fun():
    sum1 = 0
    n = input('How many Number do you want to enter: ')
    for i in range(0,int(n)):
        no = input('Num: ')
        sum1 = sum1 + no
        arr.append(int(no))
    return sum1


ret = fun()
print('Your Elements: ', arr)
print('Addition of all your elements are: ', ret)