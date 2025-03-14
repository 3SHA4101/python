class circle:
  def area(self):
    return 3.14*float(self.radius)*float(self.radius)
  
circle1=circle()
circle1.radius=input("enter radius")
circle1.area()
