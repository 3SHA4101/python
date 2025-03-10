def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if the string is equal to its reverse

# Example usage
word = "racecar"
print(is_palindrome(word))  # Output: True
