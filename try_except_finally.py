try:
  a=int(input("enter numbers to be divided"))
  b=int(input("enter numbers to be divided"))
  c=a/b
  print(c)
except ZeroDivisionError:
  print("can't be divided by 0")
finally:
  print("code executed")

  
