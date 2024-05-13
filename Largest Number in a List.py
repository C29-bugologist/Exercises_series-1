def find_largest(numbers):
  """This function takes a list of numbers as input and returns the largest number in the list."""
  largest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num
  return largest
