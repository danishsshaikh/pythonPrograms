class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*radius*radius
    def perimeter(self):
        return 2*3.14*radius
radius = int(input("Enter the Radius\n"))
obj = circle(radius)
print("The Area of the circle is\n",obj.area())
print("The Perimeter of the circle is\n",obj.perimeter())
