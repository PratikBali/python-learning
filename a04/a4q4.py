arr = list()
def fun():
    sum1 = 0
    n = input('How many Number do you want to enter: ')
    for i in range(0,int(n)):
        no = input('Num: ')
        arr.append(int(no))
    return arr
ret = fun()
print('elements are: ', ret)

# arr = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

# apply filter
filtered2 = list(filter(lambda no : (no % 2 == 0), arr))
print('filtered elements  are: ', filtered2)

# apply map
modified2 = list(map(lambda no : (no * no), filtered2))
print('modified elements  are: ', modified2)

# apply map
reduced2 = reduce(lambda a,b : a + b, modified2)
print('reduced value is ', reduced2)
