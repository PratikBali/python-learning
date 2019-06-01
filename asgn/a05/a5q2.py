def CountWords(param):
    s2 = param
    length = len(s2)
    i = 0
    cnt = 0
    print('length', length)

    while i != length:
        if s2[i] == ' ':
            i += 1
        else:
            cnt += 1
            i += 1
            while s2[i] != ' ':
                i += 1

    return cnt

stringInput = input('Enter string: ')
ret = CountWords(stringInput)
print(ret)
