user_input = input("Enter a string: ")
original_string = user_input.lower()
reversed_string = user_input[::-1].lower()
if original_string == reversed_string:
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")
