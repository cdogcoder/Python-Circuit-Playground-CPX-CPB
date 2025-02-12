# Challenge 1
# Inside of the main function block, we call the greet function three times
# with three different arguments passed (the values between the parentheses
# in each function call). The greet function takes an argument 'lang' and uses
# it to return an appropriate greeting based on the value of the argument, which
# is passed back to the point from which the function was called. In other words,
# print(greet('en'), 'Glenn') is actually equal to print('Hello', 'Glenn') after 
# the function has been executed

def greet(lang):
  if lang == 'es':
    return'Hola'
  elif lang == 'fr':
    return'Bonjour'
  else:
    return'Hello'

def main():
    print(greet('en'),'Glenn')
    print(greet('fr'),'Sabine')
    print(greet('es'),'Carlos')
    
main()

# Challenge 2

def greet2(lang):
  if lang == 'es':
    return'Hola'
  elif lang == 'fr':
    return'Bonjour'
  elif lang == 'vn':
    return 'Xin chao'
  elif lang == 'kr':
    return '안녕하세요'
  else:
    return'Hello'

def main():
    print(greet2('en'),'Glenn')
    print(greet2('fr'),'Sabine')
    print(greet2('es'),'Carlos')
    print(greet2('vn'),'Minh')
    print(greet2('kr'),'Seunghyo')
    
main()

# Challenge 3

user_name = input("What is your name?: ")
user_lang = input("What is your language?: ")
print(greet2(user_lang), user_name)
