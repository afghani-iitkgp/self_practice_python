

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


# Class for Dog
class Dog:
       
    # Class Variable
    animal = 'dog'     
       
    # The init method or constructor
    def __init__(self, breed):
           
        # Instance Variable
        self.breed = breed            
   
    # Adds an instance variable 
    def setColor(self, color):
        self.color = color
       
    # Retrieves instance variable    
    def getColor(self):    
        return self.color   
   
class Begusarai:

    # def __init__(self):
    #     #constructor function/method
        

    def aparajita(n):
        print(n)

    def juhi(arr):
        for i in range(len(arr)):
            print(i)
    
    def neha_dadpur(d):
        print(d)


if __name__ == "__main__":
    # # sqr = Square(4)
    # # print(sqr.area())
    # cub = Cube(3)
    # cub.surface_area()
    # cub.volume()



    # # Driver Code
    # Rodger = Dog("pug")
    # Rodger.setColor("brown")
    # print(Rodger.getColor()) 

    # Instantiate a class. Creating an object of a class.
    beg = Begusarai()
    amit = Begusarai()
    amit.aparajita(10)
    amit.juhi( [12,3,4,11] )
    
    beg.aparajita(n)
    beg.juhi( [0,1,2,3,4,5] )
