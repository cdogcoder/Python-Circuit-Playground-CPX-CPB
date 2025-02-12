# Challenge 4

def my_math(x,y,op):
  if op == "+":
    return x + y
  elif op == "-":
    return x - y 
  elif op == "*":
    return x * y
  else: 
    return x / y

def main():
  my_num_1 = 5
  my_num_2 = 2
  sum = my_math(my_num_1, my_num_2, "+")
  print("The sum of", my_num_1, "+", my_num_2, "=",sum)

main()

# Challenge 5
# Note: I did not implement error or exception handling in this challenge
# because the flow of the program relies on repeatedly asking the user for
# valid inputs for the operation (assuming value inputs were not given initially),
# not running into raised exception errors, which stop the execution of the program
# all together

def my_math(x,y,op):
  if op == "+":
    return x + y
  elif op == "-":
    return x - y 
  elif op == "*":
    return x * y
  else: 
    return x / y

def main():
    operations = ("+", "-", "*", "/")
    while True:
        my_num_1 = input("Num 1: ")
        my_num_2 = input("Num 2: ")
        op = input("Operation: ")
        if not my_num_1.isdigit() or not my_num_2.isdigit() or op not in operations:
            my_num_1 = input("Num 1: ")
            my_num_2 = input("Num 2: ")
            op = input("Operation: ")
        sum = my_math(float(my_num_1), float(my_num_2), op)
        print("The sum of", my_num_1, op, my_num_2, "=",sum)
        break
main()
