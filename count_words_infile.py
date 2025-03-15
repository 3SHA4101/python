def countwrd(filepath):
  try:
    with open("filepath",'r')as a:
      w=a.read()
      return len(w.splitlines())
  except FileNotFoundError:
    print(f"Error: The file '{filepath}' does not exist.")
  except Exception as e:
    print("An error occurred:", e)

# Example Usage
filepath = "example.txt"  # Change this to your file name
countwrd(filepath)   
