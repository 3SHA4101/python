def add():
  a=int(input("enter numbers to be divided"))
  b=int(input("enter numbers to be divided"))
  if b==0:
    raise ZeroDivisionError("can't be divided by 0")
  return a/b
try:
  res=add()
  print(res)
except ZeroDivisionError :
  print("can't be divided by 0")
finally:
  print(" code done")
