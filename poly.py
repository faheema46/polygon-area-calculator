class square:

    def __init__(self,side):
        self.side=side
    def area(self):
        print("My area is:",self.side**2)

class triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print("My area is:",self.base*self.height*1/2)

class rectangle:
    def __init__(self,lenght,breadth):
        self.lenght=lenght
        self.breadth=breadth
    def area(self):
        print("My area is:",self.breadth*self.lenght)

class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("The area is:",3.14*self.radius**2)

ob1=square(40)
ob2=triangle(32,29)
ob3=rectangle(15,22)
ob4=circle(56)

for shape in(ob1,ob2,ob3,ob4):
  shape.area()

    