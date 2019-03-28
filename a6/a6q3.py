class Arithmatic():

    def Addition(self, no1, no2):
        return int(no1) + int(no2)

    def Substraction(self, no1, no2):
        return int(no1) - int(no2)

    def Multiplication(self, no1, no2):
        return (int(no1) * int(no2))

    def Division(self, no1, no2):
        return int(no1) / int(no2)

    def Accept(self):
        no1 = input('Enter number no1: ')
        no2 = input('Enter number no2: ')
        return no1,no2

obj = Arithmatic()
no1,no2 = obj.Accept()

param = obj.Addition(no1,no2)
print('Addition', param)

param = obj.Substraction(no1,no2)
print('Substraction', param)

param = obj.Division(no1,no2)
print('Division', param)

param = obj.Multiplication(no1,no2)
print('Multiplication', param)


