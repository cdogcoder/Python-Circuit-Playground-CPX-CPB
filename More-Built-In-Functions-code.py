# Returns the absolute value of the user's input if it is a digit, otherwise print out "Not a number" using the abs() function
user_input = input("Enter a number please: ")
if user_input.isdigit():
  print(abs(int(user_input))
else:
  print("Not a number")

# Prints out the binary version of the user's input (assumes input is already an integer) and "You should use this hex code: {hex version of user's input}" using the bin() and hex() functions
user_input = int(input("Enter a number please: "))
print(bin(user_input))
print("You should use this hex code: ", hex(user_input))

# Prints out "Elon Musk's son's name is X Æ A-Xii" using the chr() function
print("Elon Musk's son's name is X " + str(chr(0xC6)) + " A-Xii")

# Asks for user to input a decimal number and prints out that number rounded to 2 decimal places using the round() function
user_input = int(input("Enter a decimal number please: "))
print(round(user_input, 2))

# Prints out "The equation 3 + 2 = 5" using the eval() function
print("The equation 3 + 2 =", eval("3+2"))

# Prints out "The length of myList is: 3" using the len() function
myList = [2,31,23]
print("The length of myList is:", len(myList))

# Prints out "The sum of myList is: 56" using the sum() function
print("The sum of myList is:", sum(myList))

  
