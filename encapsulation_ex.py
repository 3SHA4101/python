class cat:
  def __init__(self):
    self.krish="te"
    self.__ram="krish"
  def trish(self):
    print(self.__ram)
call=cat()
print(call.krish)
call.trish()  #to call private we have to mention the perticular function 
