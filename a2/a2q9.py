def NumDigit(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    return count

n=int(input("Enter number:"))
ret = NumDigit(n);
print("The number of digits in the number are:",ret)