class car:
  def __init__(self,name,clr,speed):
    self.name=name
    self.clr=clr
    self.speed=speed

  def nam(self):
    return self.name
  def colr(self):
    return self.clr
  def speeed(self):
    return self.speed
c1=car("swift","blue",150)
c2=car("tarzan","red",180)

print(c1.colr())
print(c1.speeed())
print(c2.nam())
print(c2.speeed())
print(c2.colr())
