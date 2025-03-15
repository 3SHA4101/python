def copy(sourcefile,destinationfile):
  try:
    with open("sourcefile",'r')as a:
      content=a.read()
  
    with open("destinationfile",'w')as b:
      a.write(content)
    print(f"Content copied from '{sourcefile}' to '{destinationfile}' successfully.")
  except FileNotFoundError:
    print(f"Error: File '{sourcefile}' not found.")
  except Exception as e:
    print(f"An error occurred: {e}")
sourcefile=input("enter source file name")
destinationfile=input("enter destination file name")
copy(sourcefile,destinationfile)
