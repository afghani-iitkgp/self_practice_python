
# https://realpython.com/python-super/
class Rectangle:
    def __init__(self, length, width):
        self.len = length
        self.wid = width
    
    def area(self):
        return self.len * self.wid
    
    def perimeter(self):
        return 2 * (self.len + self.wid)


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, side_len):
        super().__init__(side_len, side_len)


class Cube(Square):

    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        face_area = super().area()
        return face_area * self.side_len


if __name__ == "__main__":
    # sqr = Square(4)
    # print(sqr.area())
    cub = Cube(3)
    cub.surface_area()
    cub.volume()