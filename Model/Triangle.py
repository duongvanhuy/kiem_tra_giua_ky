import Model.Shape as Shape


class Triangle(Shape.Shape):
    # tạo thuộc tính 3 cạnh
    def __init__(self, x, y, a, b, c):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    # hàm tostring
    def __str__(self):
        return "Triangle: x = " + str(self.x) + ", y = " + str(self.y) + ", a = " + str(self.a) + ", b = " + str(self.b) + ", c = " + str(self.c)
