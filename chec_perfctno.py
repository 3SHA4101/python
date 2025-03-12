def is_perfect(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Example Usage
num = int(input("Enter a number: "))
print("3sha-31")
if is_perfect(num):
    print(f"{num} is a Perfect Number")
else:
    print(f"{num} is NOT a Perfect Number")
