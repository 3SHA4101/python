class student:
  def __init__(self,name):
    self.name=name
  def passornot(self,marks):
    if marks>=20:
      print("u r pass")
    else:
      print("u r fail")
a=student(a)
a.name=input("enter name")
a.marks=int(input("enter marks"))
a.passornot(a.marks)
