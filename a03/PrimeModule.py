def ChkPrime(no):
    flag = 0

    if no == 1:
        return 1
    else:
        half = no / 2

        if half == 1:
            return no
        else:
            for i in range(2,int(half)):
                if no % i != 0:
                    flag = no
                    continue
                else:
                    flag = 0
                    break

    return flag