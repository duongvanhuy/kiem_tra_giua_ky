import Model.Shape as Shape


class Circle(Shape.Shape):
    # tạo thuộc tính bán kính
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    # hàm tostring
    def __str__(self):
        return "Circle: x = " + str(self.x) + ", y = " + str(self.y) + ", radius = " + str(self.radius)
