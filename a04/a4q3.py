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

# apply filter with function
def find(no):
    return (no >= 70 and no <= 90)
filtered1 = list(filter(find, arr))
print('filtered elements with function are: ', filtered1)

# apply filter without function
filtered2 = list(filter(lambda no : (no >= 70 and no <= 90), arr))
print('filtered elements without function are: ', filtered2)

# apply map with function
def modify(no):
    return (no + 10)
modified1 = list(map(modify, filtered1))
print('modified elements with function are: ', modified1)

# apply map without function
modified2 = list(map(lambda no : (no + 10), filtered2))
print('modified elements without function are: ', modified2)

# apply reduce with function
def reduceit(a,b):
    return (a * b)
reduced1 = reduce(reduceit, modified1)
print('reduced value with function is: ', reduced1)

# apply map without function
reduced2 = reduce(lambda a,b : a * b, modified2)
print('reduced value without function is: ', reduced2)
