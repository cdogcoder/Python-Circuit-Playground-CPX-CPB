# Python Dictionaries

# The difference between lists and dictionaries is that lists are indexed using integer numbers, while dictionaries are
# indexed by a string value. Additionally, dictionaries do not have any inherent order the way that lists do, as lists
# are numbered and dictionaries use strings of characters as their index method. You index both structures the same way
# (using square brackets) like so: my_list[0] and my_dict['name']. Please look at the bottom of the script for my added
# code.

print('''
Python Dictionaries - Lists vs. Dictionaries 
Dictionaries are Key:Value pairs of objects in 
a list like structure.

Challenge #1
Run the code, Explain the difference between lists and dictionaries

- See that the list is index'able
- See that the Dictionary is a keyword:value pair

- How do you "index" a dictionary?

- Add an additional key:value pair to the ddd dictionary
  Imagine that this is a dictionary for a college engineering class.  
  Does it have a lab? 'lab':'true' , add a short description for 
  the class. 'description':'short string describing the class'

      ''')

lst = list()
lst.append(183)
lst.append("2:00 PM")
print(lst)
lst[1] = "3:00 PM"
print(lst)
print(lst[1])

ddd = dict()
ddd['course'] = 182
ddd['time'] = "2:00 PM"
print(ddd)
ddd['time'] = "3:00 PM"
print(ddd)
print(ddd['time'])

ddd['lab'] = True
ddd['description'] = "Mechanical Engineering + Electrical Engineering = Fire Breathing Robots!"
print(ddd)
