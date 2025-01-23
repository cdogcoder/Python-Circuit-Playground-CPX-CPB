kevin = "kevin"

def myKevin():
  print("I love", kevin)

myKevin()

def myKevin2():
  kevin = "KEVIN"
  print("I love", kevin)

myKevin()
print("I love", kevin)

def myKevin3():
  global kevin
  print("I love", kevin)

myKevin3()
print("I love", kevin)
