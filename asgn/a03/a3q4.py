arr = list()

def fun(n):
    frequency = 0

    # accept list
    for i in range(0,int(n)):
        no = input('Num: ')
        arr.append(int(no))

    search = input('Enter no search: ')

    for i in arr:
        print(i)
        if i == search:
            frequency = frequency + 1
        else:
            frequency = 0

    return frequency

# accept total no
n = input('Enter no of elements: ')

# call
ret = fun(n)

print('List', arr)

print('frequency', ret)
