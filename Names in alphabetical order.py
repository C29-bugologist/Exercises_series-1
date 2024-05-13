names = []
while True:
  user_input = input("Enter a name (or 'q' to quit): ")
  if user_input.lower() == 'q':
    break
  # Validate input to ensure it's a string
  if not user_input.isalpha():
    print("Invalid input. Please enter a name (letters only).")
    continue
  names.append(user_input)

# Sort the names in alphabetical order
names.sort()

print("\nNames in alphabetical order:")
for name in names:
  print(name)

