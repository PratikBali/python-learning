def ChkPrime(no):
    flag = 0

    if no == 1:
        return 1
    else:
        half = no / 2

        if half == 1:
            return no
        else:
            for i in range(2,int(half)+1):
                if no % i != 0:
                    flag = no
                    continue
                else:
                    print(no,' is divisible by', i)
                    flag = 0
                    break

    if flag != 0:
        print('prime', flag)
        return flag

def ChkMax(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2