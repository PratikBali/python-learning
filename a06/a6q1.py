class Demo():
    value = 0

    def __init__(self, num1, num2):
        self.no1 = num1
        self.no2 = num2

    def Fun(self):
        print(self.no1)
        print(self.no2)

    def Gun(self):
        print(self.no1)
        print(self.no2)

Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()


