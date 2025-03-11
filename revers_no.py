a=int(input("enter numbers"))
for i in range(a):
  value = input(f"enter value of {i}: ") # Use f-string for formatting and assign input to variable
  print(value)  # Print the entered value
  i=-1 # This line is not needed and can be removed
  print(i)
