class animal:
  def speak(self):
    print("cute animal")
  def tells(self):
    print("u r cute")

class cat(animal):
  pass
dog=cat()
dog.speak()
dog.tells()
