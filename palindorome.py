def is_palindrome(s: str) -> bool:
  return s == s[::-1]

print(is_palindrome("level"))   # True
print(is_palindrome("python"))  # False
print(is_palindrome("abba"))    # True
