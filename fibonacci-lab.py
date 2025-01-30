import random
my_fibonacci = []
fib_int1 = int(input("Enter a number from 1 to 9:"))
print("User number:", fib_int1)
fib_int2 = random.randint(1, 20)
print("Random number:", fib_int2)

my_fibonacci.append(fib_int1)
my_fibonacci.append(fib_int2)

for i in range(10):
  print(my_fibonacci)
  my_fibonacci.append(my_fibonacci[i]+my_fibonacci[i+1])
  print(my_fibonacci)

print(my_fibonacci)
print("done")
