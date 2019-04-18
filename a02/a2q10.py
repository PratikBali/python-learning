def NumDigit(n):
    summ = 0;
    d = 0;
    while(n>0):
        d = n % 10
        n = n//10
        summ = summ + d;
    return summ

n=int(input("Enter number:"))
ret = NumDigit(n);
print("The addition of digits in the number are:",ret)