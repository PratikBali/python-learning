import sympy


class Arithmatic():
    numbers = 0

    def __init__(self):
        self.value = 0

    def ChkPrime(self):
        return sympy.isprime(self.value)

    def Factors(self):
        factorsList = []
        for i in range(1,self.value):
            if(self.value % i == 0):
                factorsList.append(i)
        return factorsList

    def SumFactors(self):
        sum1 = 0
        for i in range(1,self.value):
            if(self.value % i == 0):
                sum1 += i
        return sum1

    def ChkPerfect(self):
        sum1 = Arithmatic.SumFactors(self)
        return self.value == sum1

    def Accept(self):
        self.value = int(input('Enter number: '))
        return self.value

obj = Arithmatic()
print('number: ', obj.Accept())
print('is prime:', obj.ChkPrime())
print('factors: ', obj.Factors())
print('sum of factors: ', obj.SumFactors())
print('is perfect: ', obj.ChkPerfect())



