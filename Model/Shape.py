from abc import ABC, abstractmethod


class Shape(ABC):
    # tạo 2 thuốc tính toa độ x, y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def perimeter(self, model):
        pass

    @abstractmethod
    def area(self, model):
        pass
