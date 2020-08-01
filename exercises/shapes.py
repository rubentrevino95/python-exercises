class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi

    # method
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(30)

print (my_circle.pi)

print (my_circle.radius)

print (my_circle.get_circumference())

print (my_circle.area)


class Square():

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width

    def get_perimeter(self):
        return (self.length * 2) * (self.width * 2)


my_square = Square(4, 8)

print (my_square)

print (my_square.area)
