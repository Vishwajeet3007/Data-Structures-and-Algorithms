#Area of triangle using heroin's formula in python
import math
class Triangle:
    def __init__(self,a,b,c):
     self.a = a
     self.b = b
     self.c = c

    def calculate_area(self):
     s = (self.a + self.b + self.c)/2
     area = math.sqrt(s * (s-self.a) * (s- self.b) * (s- self.c) )
     return area
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

triangle = Triangle(side1, side2, side3)
area = triangle.calculate_area()
print("The area of the triangle is : ",area)