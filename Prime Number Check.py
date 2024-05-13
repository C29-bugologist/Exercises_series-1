number = int(input("Enter a number: "))
isPrime = True  # Assume prime initially
if number <= 1:
  isPrime = False
else:
  i = 2
  while i * i <= number:
    if number % i == 0:
      isPrime = False
      break
    i += 1
if isPrime:
  print("The number is prime.")
else:
  print("The number is not prime.")
