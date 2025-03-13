a={
    "name":"3sha",
    "age":20,
    "date":8
}

for i,j in a.items():
  print(i,j)

a["age"]=19
a["day"]="wed"
for i,j in a.items():
  print(i,j)
