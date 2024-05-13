def factorial(number):
  """This function takes a number as input and returns its factorial using recursion."""
  if number == 0:
    return 1
  else:
    return number * factorial(number - 1)
