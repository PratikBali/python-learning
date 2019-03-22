def AsciiAverage(param):
    count = 0
    k = 0
    for i in param:
        print(i, ord(i))
        k = k + ord(i)
        count += 1

    ans = k/count
    return ans

stringInput = input('Enter string: ')
ret = AsciiAverage(stringInput)
print(ret)
