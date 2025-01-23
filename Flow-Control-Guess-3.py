import random

print('This is a Guessing Game')
print("Ready to play?")

num2_guess = random.randint(1, 1000000)
user_guess = int(input("Enter a number: "))

print(num2_guess)
print(type(num2_guess))
print(user_guess)

print("Your guess was", user_guess, "and the Random Number was", num2_guess)

if num2_guess == user_guess:
  print("Good Guess, you are a Winner")
  print(user_guess, "is EQUAL to", num2_guess)
elif num2_guess == (user_guess + 1) or num2_guess == (user_guess - 1):
  print("Close, but No Cigar..")
else:
  print("BETTER LUCK NEXT TIME BUD")
  print(user_guess, "is NOT EQUAL to", num2_guess)
  
print("All Done!")
