from math import factorial

def pascal_triangle(n):
    for i in range(n):
        for j in range(n - i - 1):  # Print leading spaces
            print(" ", end=" ")
        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end="   ")
        print()  # Move to next line

# Take input for number of rows
rows = int(input("Enter number of rows: "))
pascal_triangle(rows)
