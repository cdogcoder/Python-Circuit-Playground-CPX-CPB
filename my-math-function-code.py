# Challenge 1
# The my_num_1 and my_num_2 variables are passed as arguments to the my_math function call inside of the main function's body
# When the main function is called, it calls the my_math function with the my_num_1 and my_num_2 variables as arguments
# The my_math function returns the sum of the two arguments it was passed and passes it back to the point where the function
# was initially called
# In other words, sum = my_math(my_num_1, my_num_2) becomes sum = 7 once the my_math function has been executed

def my_math(x,y):
  z=x+y
  return z

def main():
  my_num_1 = 5
  my_num_2 = 2
  sum = my_math(my_num_1, my_num_2)
  print("The sum of", my_num_1, "+", my_num_2, "=",sum)

main()

# Challenge 2
def multiply(num1, num2):
    return num1 * num2

# Challenge 3
def alwaysEven(num1, num2):
    sum = num1 + num2
    if sum % 2 == 0:
        return sum
    return sum + 1
