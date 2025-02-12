# Challenge 1
# Tuples are created and indexed the same way as lists are
# except that tuples are created using parentheses. The indexing
# works the same way; for example, my_tuple[0] will return the first element of
# the tuple
def sum_and_avg(t):
    x,y,z,zz = t
    s = x + y + z +zz
    a = s/4
    return(s, a,)
# see that the type( of the function is <tuple>)
print('--------------------------------------')
print('This is the value of the Tuple returned')
#(sum, avg) = sum_and_avg(3, 16, 7,)
my_tuple = (2, 9, 42,76,)
x = sum_and_avg(my_tuple)
print(x)
sum = x[0]
avg = x[1]
print('Sum =', sum)
print('Sum is of type',type(sum))
print('Avg =', avg)
print('Avg is of type',type(avg))

# Challenge 2 & 3 (they are the same challenge)
def sum_and_avg2(t):
    x,y,z = t
    s = x + y + z
    a = s/3
    return(s, a,)

my_tuple = (2, 6, 42)
x = sum_and_avg2(my_tuple)
print(x)
(sum, avg) = sum_and_avg2(x)
print('Sum =', sum)
print('Sum is of type',type(sum))
print('Avg =', avg)
print('Avg is of type',type(avg))

