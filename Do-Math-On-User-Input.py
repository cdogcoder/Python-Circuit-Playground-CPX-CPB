while True:
  user_input = input("Enter a whole number greater than or equal to 20: ")
  if user_input.isdigit() and int(user_input) >= 20:
    user_input = int(user_input)
    break
count = 0
while user_input > 1:
  user_input /= 2
  count += 1
  print("The current value of the user input after some math is", user_input)
  print("The while loop has looped", count, "times")
