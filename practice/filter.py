arr = [1,2,3,4,5,6,7,8,9]

# method 1
def chkeven(no):
    if (no % 2 == 0):
        return True
    else:
        return False

ret = list(filter(chkeven, arr))
print(ret)

# method 2
def chkeven2(no):
    return no % 2 == 0

ret2 = list(filter(chkeven2, arr))
print(ret2)

#  method 3
def chkeven3(no):
    print(no)
    return lambda no : no % 2 == 0

ret3 = chkeven3(arr)
print(ret3)

# method 4
ret4 = lambda no : no % 2 == 0
# print(ret4(arr))




