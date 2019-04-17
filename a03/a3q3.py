arr = list()

def fun(n):
    for i in range(0,int(n)):
        no = input('Num: ')
        arr.append(int(no))
        if i == 0:
            min1 = arr[i]
        else:
            min2 = arr[i]
            if min2 < min1:
                min1 = min2

    return min1

n = input('Enter no of elements: ')
ret = fun(n)
print('List', arr)
print('min', ret)
