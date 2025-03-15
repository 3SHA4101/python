def countlin(filepath):
  try:
    with open("filepath",'r')as a:
      count=sum(1 for line in a)
      print(f"lenth ={count}")
  except FileNotFoundError:
    print(f"Error: The file '{filepath}' does not exist.")
  except Exception as e:
    print("An error occurred:", e)

# Example Usage
filepath = "example.txt"  # Change this to your file name
countlin(filepath)   

  
