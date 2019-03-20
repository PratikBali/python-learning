def pow(n):
    fp = lambda n : n * n
    ret = fp(n)
    return ret

n = input('Enter number: ')
ret = pow(n)
print('By applying power of 2: ',ret)