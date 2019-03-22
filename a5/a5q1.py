def ReverseString(param):
    # concatenation using for loop
    s1 = ''
    for i in param:
        s1 = i + s1

    # slicing
    s2 = param[::-1]

    # recursion using slicing
    def recursion(s):
        if len(s) == 0:
            return s
        else:
            # print(s, s[1:], s[0], ((s[1:]) + s[0]))
            return recursion(s[1:]) + s[0]
    s3 = recursion(param)

    # revwesed method
    def usereversed(string):
        string = "".join(reversed(string))
        return string
    s4 = usereversed(param)


    return s1,s2,s3,s4

anystr = input('Enter any string to reverse: ')
ret = ReverseString(anystr)

print(ret)
print(type(ret))