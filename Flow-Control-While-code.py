print(x)

x = x + 1
print(x)

x = 0
x = x + 1
print(x)

x = 5
print(x)
x += 1
print(x)

windows_are_dirty = 0
while windows_are_dirty > 0 :
  print("Wipe On")
  print("Wipe Off")
print("Windows are Clean")

windows_are_dirty = 5
while windows_are_dirty > 0 :
  print("Wipe On")
  print("Wipe Off")
print("Windows are Clean")

windows_are_dirty = 5
while windows_are_dirty > 0 :
  print("Wipe On")
  print("Wipe Off")
  windows_are_dirty -= 1
print("Windows are Clean")

n = 5
print('Say Cheese...')
while n > 0:
  print(n)
  n = n - 1
print("Click!")

n = 5
x = True # Boolean T/F
print('Say Cheese...')
while x :
  print(n)
  n = n - 1
print("Click!")

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

x = 5
y = 3
while True:
  # Do Something
  print('x =',x,'\ny =',y)
  z = x + y
  print('x + y = ',z)
  if (z == 11) :
    break
  x +=1
  print('y is still',y,'but x is now',x)
print('Done!')
