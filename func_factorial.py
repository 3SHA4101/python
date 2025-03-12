def factorial():
  a=int(input("enter start range"))
  b=int(input("enter end range"))
  fact=1
  for i in range(a,b+1):
    fact=fact*i
  print(fact)
