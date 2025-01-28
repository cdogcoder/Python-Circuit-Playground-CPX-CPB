print('This is a Guessing Game')
print("Ready to play?")

num2_guess = 120

# try block will try to convert the user input into an integer
# if an error occurs in the try block, the except block will print out a message saying that the user's input was not a number

try:
  user_guess = int(input("Enter a number: "))
  print("Thanks for guessing with the number", user_guess)
except:
  print(user_guess, "is not a number")
  

print(num2_guess)
print(type(num2_guess))
print(user_guess)

if num2_guess == user_guess:
  print("Good Guess, you are a Winner")
else:
  print("BETTER LUCK NEXT TIME BUD")

print("All Done!")
