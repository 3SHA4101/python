my_dict = {"a": 1, "b": 2, "c": 3}

key = input("enter to find")

if key in my_dict:
    print(f"Key '{key}' is present in the dictionary.")
else:
    print(f"Key '{key}' is not present in the dictionary.")
