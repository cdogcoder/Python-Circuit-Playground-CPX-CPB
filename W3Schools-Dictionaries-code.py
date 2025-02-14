my_fav_dict = {
    "name": "John Doe",
    "age": 20,
    "date of birth": "1/1/2000",
    "year": 2020,
    "car": "Honda Accord",
    "year": 2025,
    "age": 25,
    "favorite foods": ["rice", "cookies", "cake"]
}

my_other_fav_dict = dict(name="Jane Doe", age=27, country="America")

print(my_fav_dict['age'])
print(len(my_fav_dict))
print(type(my_fav_dict))

for key in my_fav_dict.keys():
    print(key, my_fav_dict[key])
