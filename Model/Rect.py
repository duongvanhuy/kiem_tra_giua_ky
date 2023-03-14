import Model.Shape as Shape


class Rect(Shape.Shape):
    # tạo thuộc tính chiều dài và chiều rộng
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    # hàm tostring

    def __str__(self):
        return "Rect: x = " + str(self.x) + ", y = " + str(self.y) + ", width = " + str(self.width) + ", height = " + str(self.height)
