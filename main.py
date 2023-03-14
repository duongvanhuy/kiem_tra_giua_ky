import random
from Model.Rect import Rect
from Model.Circle import Circle
from Model.Triangle import Triangle


class Main:
    # tạo 1 danh sách đối tượng Rect, Circle, Triangle
    rects = []
    circles = []
    triangles = []

    # fake dữ liệu
    def generateData(self, n):
        file = open("data.txt", "w")
        shapes = ["Rect", "Circle", "Triangle"]
        shape_counts = {"Rect": 0, "Circle": 0, "Triangle": 0}
        for i in range(n):
            shape = shapes[i % len(shapes)]
            if shape == "Rect":
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                width = random.randint(1, 10)
                height = random.randint(1, 10)
                file.write(
                    f"#Rect\n{str(width)} {str(height)}\n{str(x)} {str(y)}\n")
                shape_counts["Rect"] += 1
            elif shape == "Circle":
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                radius = random.randint(1, 10)
                file.write(f"#Circle\n{str(radius)} \n{str(x)} {str(y)}\n")
                shape_counts["Circle"] += 1
            elif shape == "Triangle":
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                if (a + b > c and a + c > b and b + c > a):
                    file.write(
                        f"#Triangle\n{str(a)} {str(b)} {str(c)}\n{str(x)} {str(y)}\n")
                    shape_counts["Triangle"] += 1
                else:
                    i -= 1
            if all(count == 10 for count in shape_counts.values()):
                break
        file.close()

    # hàm dùng để đọc dữ liệu từ file txt => in ra màn hình theo từng dòng
    def readData(self):
        # đọc dữ liệu từ file txt
        file = open("data.txt", "r")
        lines = file.readlines()
        file.close()
        # duyệt từng dòng trong file txt
        for i in range(len(lines)):
            # nếu là hình chữ nhật
            if lines[i] == "#Rect\n":

                # lấy chiều dài và chiều rộng
                width = int(lines[i + 1].split(" ")[0])
                height = int(lines[i + 1].split(" ")[1])
                # lấy ra toạn độ
                x = int(lines[i + 2].split(" ")[0])
                y = int(lines[i + 2].split(" ")[1])
                # tạo 1 đối tượng Rect
                rect = Rect(x, y, width, height)
            # nếu là hình tròn
            elif lines[i] == "#Circle\n":
                # lấy bán kính
                radius = int(lines[i + 1])
                x = int(lines[i + 2].split(" ")[0])
                y = int(lines[i + 2].split(" ")[1])
                # tính chu vi và diện tích
                # tao 1 đối tượng Circle
                circle = Circle(x, y, radius)
                # thêm đối tượng Circle vào danh sách
                self.circles.append(circle)

            # nếu là hình tam giác
            elif lines[i] == "#Triangle\n":
                # lấy 3 cạnh
                a = int(lines[i + 1].split(" ")[0])
                b = int(lines[i + 1].split(" ")[1])
                c = int(lines[i + 1].split(" ")[2])

                x = int(lines[i + 2].split(" ")[0])
                y = int(lines[i + 2].split(" ")[1])
                # tạo 1 đối tượng Triangle
                triangle = Triangle(x, y, a, b, c)
                # thêm đối tượng Triangle vào danh sách
                self.triangles.append(triangle)

    # hàm liệt kê hình có chu vi lớn nhất, diện tích lớn nhất
    def maxPerimeter_Area(self):
        # khởi tạo các biến
        maxPerimeter = 0
        maxArea = 0
        maxPerimeterShape = ""
        maxAreaShape = ""
        # viết tiếp tìm ra hình có chu vi lớn nhất , tìm ra hình có diện tích lớn nhất trong 3 danh sách
        for rect in self.rects:
            if rect.perimeter() > maxPerimeter:
                maxPerimeter = rect.perimeter()
                maxPerimeterShape = rect
            if rect.area() > maxArea:
                maxArea = rect.area()
                maxAreaShape = rect
        for circle in self.circles:
            if circle.perimeter() > maxPerimeter:
                maxPerimeter = circle.perimeter()
                maxPerimeterShape = circle
            if circle.area() > maxArea:
                maxArea = circle.area()
                maxAreaShape = circle
        for triangle in self.triangles:
            if triangle.perimeter() > maxPerimeter:
                maxPerimeter = triangle.perimeter()
                maxPerimeterShape = triangle
            if triangle.area() > maxArea:
                maxArea = triangle.area()
                maxAreaShape = triangle
      # in ra màn hình hình có chu vi lớn nhất và diện tích lớn nhất
        print(
            f"Hình có chu vi lớn nhất là: {maxPerimeterShape.__str__()} với chu vi là: {str(maxPerimeter)}")
        print(
            f"Hình có diện tích lớn nhất là: {maxAreaShape.__str__()} với diện tích là: {str(maxArea)}")

    # kiểm tra số lượng hình nằm chồng lên nhau nhiều nhất theo tạo độ ( x, y) tính cả các hình khác nhau
    # def maxOverlap(self, lines):


obj = Main()
# obj.generateData(30)
obj.readData()
obj.maxPerimeter_Area()
