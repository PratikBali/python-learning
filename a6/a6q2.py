class Circle():
    PI = 3.142

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumferrence = 0.0

    def Accept(self):
        self.radius = input('Enter radius : ')

    def CalculateArea(self):
        self.area = Circle.PI * (int(self.radius) * int(self.radius))

    def CalculateCircumference(self):
        self.circumferrence = 2 * int(Circle.PI) * int(self.radius)

    def Display(self):
        print('Radius of circle: ', self.radius)
        print('Area of circle: ', self.area)
        print('Circumference of circle: ', self.circumferrence)

if __name__ == '__main__':
    circle = Circle()
    circle.Accept()
    circle.CalculateArea()
    circle.CalculateCircumference()
    circle.Display()

