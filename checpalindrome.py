def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if the string is equal to its reverse

# Get user input
word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
