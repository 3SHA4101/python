a=int(input("enter start range"))
b=int(input("enter end range"))
evensum=0
for i in range(a,b+1):
  if i%2==0:
    evensum=evensum+i
print(evensum)
    
