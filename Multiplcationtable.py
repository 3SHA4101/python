def multiplication_table(num):
    print(f"Multiplication Table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Taking user input
num = int(input("Enter an integer: "))
multiplication_table(num)
