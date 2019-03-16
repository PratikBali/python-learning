def chkPrime(num):
    flag = 0;
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                flag = 1;
                break
            else:
                flag = 0;

        if flag == 0:
            print(num,"is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")

chkPrime(12);
chkPrime(5);
chkPrime(17);
chkPrime(22);