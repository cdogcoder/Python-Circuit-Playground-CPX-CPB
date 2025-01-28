try:
  print(kevin)
except NameError: 
  print("KEVIN!")
except TypeError:
  print("NOOOOOOOOOOOOOOOO")
except: 
  print("I like cars")
else:
  print("You're chilling")
finally:
  print("I'm here too..")

kevin = "howard"

if kevin == "kevin":
  raise Exception("Hi Kevin")
