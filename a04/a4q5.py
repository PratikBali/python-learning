from Module import *

# arr = list()
# def fun():
#     sum1 = 0
#     n = input('How many Number do you want to enter: ')
#     for i in range(0,int(n)):
#         no = input('Num: ')
#         arr.append(int(no))
#     return arr
# ret = fun()
# print('elements are: ', ret)

arr = [5, 7, 3, 76, 68, 24, 89, 23, 86, 90, 45, 143]

# apply filter
filtered = list(filter(ChkPrime, arr))
print('filtered elements  are: ', filtered)

# apply map
modified = list(map(lambda no : (no * 2), filtered))
print('modified elements  are: ', modified)

# apply map
reduced = reduce(ChkMax, modified)
print('reduced value is: ', reduced)
