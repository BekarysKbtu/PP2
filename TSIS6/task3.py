def is_palindrome(string):
    return string == string[::-1]

input_string = str(input())
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
