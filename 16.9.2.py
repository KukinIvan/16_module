class Rectangle:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a*self.b
 
rect_1 = Rectangle(5,10)

print(rect_1.get_area())