class circle:
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    return 3.14*float(self.radius)*float(self.radius)
  
circle1=circle("3")
circle1.area()
