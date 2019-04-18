def fact(num):
    factorial = 1;
    sum = 0;
    for i in range(1, num):
        if (num % i == 0):
            print(i)
            sum = sum + i;
    print("The sum of factorial of",num,"is",sum)

fact(12);