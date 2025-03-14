class vehicle:
  def name(self,):
   a=input("enter name of vehicle")
   print(f"vehicle name={a}")
class v1:
  def milage(self):
    b=input("enter milage of vehicle")
    print(f"vehicle name={b}")
class v3(vehicle,v1):
  pass
a=v3()
a.name()
a.milage()
