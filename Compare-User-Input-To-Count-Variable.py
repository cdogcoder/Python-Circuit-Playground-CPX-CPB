while True:
  user_input = input("Enter a whole number from 0-9)
  if user_input.isdigit() and user_input >= 0 and user_input <= 9:
    user_input = int(user_input)

for i in range(0,11):
  if i == user_input:
    print("The User variable is equal to the Count variable. User =", user_input, "Count variable =", i)
  else:
    print(i)
