# Challenge 1 

def sum_and_avg(num1, num2, num3):
  s = num1+num2+num3
  a = s/3
  print(type(s))
  print(type(a))
  return (s,a)


print(type(sum_and_avg(3,8,5))

# Challenge 2 & Challenge 3
def sum_and_avg2(tup):
  x,y,z = tup
  s = x+y+z
  a = s/len(tup)
  return (s,a)

my_tuple = (2,6,42)
(sum, avg) = sum_and_avg2(my_tuple)

