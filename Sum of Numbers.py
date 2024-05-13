numbers = []  # Empty list to store user input
while True:
  user_input = input("Enter a number (or 'q' to quit): ")
  if user_input == 'q':
    break
  numbers.append(int(user_input))
total = sum(numbers)
print("Sum of numbers:", total)
