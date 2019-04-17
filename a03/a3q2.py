arr = list()

def fun():
    n = input(' how many numbers do you want to enter: ')
    max1 = 0
    for i in range(0,int(n)):
        no = input('Num: ')
        if no > max1:
            max1 = no
        arr.append(int(no))
    return max1

ret = fun()
print('List', arr)
print('max', ret)
