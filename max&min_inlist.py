n=int(input("how many elements in list u want"))
mylist=[]
for i in range(n):
  a=int(input(f"enter {i} element"))
  mylist.append(a)

print("created list=",mylist)

mylist.sort()
b=len(mylist)
print("min number is")
print(mylist[0])
print("max number is")
print(mylist[b-1])
