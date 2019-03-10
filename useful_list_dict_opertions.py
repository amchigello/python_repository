import copy
import timeit
import collections
import operator
list1 = ['Apple', 'Grapes', 'Oranges',
         'Banana', 'Watermelon', 'Mango',
         'Mango', 'Grapes']

# Return the occurences of items
occurences = dict(collections.Counter(list1))
print(occurences)

# Return the occurences of one particular item
print(list1.count('Grapes'))

# Key with max values
max_value = max(occurences.values())
max_keys = [key for key, value in occurences.items() if value == max_value]
print(max_keys)

# Reverse a list
print(list1[::-1])

# Apply funtion to all items of a list
upper_list = map(lambda x: x.upper(), list1)
print(list(upper_list))

# Covert a list into dictionary by applyinga function
vegetables = ['Broccoli', 'Cabbage', 'Cauliflower', 'Carrot']
length_list = map(lambda x: len(x), vegetables)
print(dict(zip(vegetables, length_list)))

# Return index of an element in list
print(list1.index('Grapes'))
print([key for key, value in enumerate(list1) if value == 'Grapes'])

# Compare list
city1 = ['Bangalore', 'Mangalore', 'Mysore']
city2 = ['Mysore', 'Bangalore', 'Mangalore']
city3 = ['Bangalore', 'Mangalore', 'Mysore', 'Panaji']
city4 = ['Bangalore', 'Mangalore', 'Mysore', 'Panaji']


def cmp(l1, l2):
    if l1 == l2:
        return True
    return False


print(cmp(city1, city2))
print(cmp(city1, city3))
print(cmp(city3, city4))

# Set operations on python
animals1 = {"Cat", "Dog", "Goat"}
animals2 = {"Cat", "Dog", "Sheep"}

print("A union B is {}".format(animals1 | animals2))
print("A intersect B is {}".format(animals1 & animals2))
print("A minus B is {}".format(animals1 - animals2))
print("A symmetric diff B is {}".format(animals1 ^ animals2))

# Operate on successive list elements
test_list = [1, 4, 5, 3, 6]
print(list(zip(test_list[: -1], test_list[1:])))
res = [test_list[i + 1] - test_list[i] for i in range(len(test_list)-1)]
res = [j - i for i, j in zip(test_list[: -1], test_list[1:])]
print(res)

##############################################

# Dictionary

car1 = {'name': 'XUV', 'type': 'suv', 'seats': 7, 'color': 'silver'}
car2 = {'name': 'XUV', 'type': 'suv', 'seats': 5, 'fuel': 'petrol'}

# loop through keys and values
for k, v in car1.items():
    print("The value of {} is {}".format(k, v))


print(list(car1.keys()))
print(list(car1.values()))
# getting values from keys and viceversa

print([key for (key, value) in car1.items() if value == 'silver'])
veggies = {'Carrot': 20, 'Beetroot': 15, 'Broccoli': 80, 'Spinach': 10, 'Cabbage': 25, 'Cauliflower': 30, 'Brinjal': 20}
vals=[20,15]
print([key for key in veggies.keys() if veggies[key] in vals])

def get_keys(dict_val, val):
    for k, v in dict_val.items():
        if v == val:
            return k
    return None


print(get_keys(car1, 7))
print(get_keys(car1, 'XUV'))
print(get_keys({'name': 'nayak',
                'city1': 'mysore',
                'city2': 'mysore'}, 'mysore'))

# existence check
print('fuel' in car2)

# Unlike copy(), the assignment operator does deep copy.
x = {"a": 1}
y = x.copy()
print(id(x))
print(id(y))


###########different ways of creating dictionary#############
name = ['Pandu', 'Sai', 'Vinod', 'Pankaj']
age = [24, 25, 26, 27]
city = ['Mangalore', 'Bangalore', 'Channapattana', 'Nagpur']

# 1: assignment
#{'Pankaj': 27, 'Vinod': 26, 'Pandu': 24, 'Sai': 25}
d1 = {}
for i in range(len(name)):
    d1[name[i]] = age[i]

# {'Pankaj': {'age': 27, 'city': 'Nagpur'}, 'Vinod': {'age': 26, 'city': 'Channapattana'}, 'Pandu': {'age': 24, 'city': 'Mangalore'}, 'Sai': {'age': 25, 'city': 'Bangalore'}}
d1 = {}
for i in range(len(name)):
    d2 = {}
    d2['age'] = age[i]
    d2['city'] = city[i]
    d1[name[i]] = d2

# 2: Using dict keyword
# {'Pankaj': {'age': 27, 'city': 'Nagpur'}, 'Vinod': {'age': 26, 'city': 'Channapattana'}, 'Pandu': {'age': 24, 'city': 'Mangalore'}, 'Sai': {'age': 25, 'city': 'Bangalore'}}
d1 = {}
for i in range(len(name)):
    d1[name[i]] = dict(city=city[i], age=age[i])

# 3: Using dict key/value tuples
# {'Pankaj': {'age': 27, 'city': 'Nagpur'}, 'Vinod': {'age': 26, 'city': 'Channapattana'}, 'Pandu': {'age': 24, 'city': 'Mangalore'}, 'Sai': {'age': 25, 'city': 'Bangalore'}}
d1 = {}
for i in range(len(name)):
    d1[name[i]] = dict([('city', city[i]), ('age', age[i])])


# 4 using fromkeys
# {'Nagpur': None, 'Bangalore': None, 'Mangalore': None, 'Channapattana': None}
dict.fromkeys(city)
# {'Nagpur': 1, 'Bangalore': 1, 'Mangalore': 1, 'Channapattana': 1}
dict.fromkeys(city, 1)

# 5 Using zip
dict(zip(name, age))  # {'Pankaj': 27, 'Vinod': 26, 'Pandu': 24, 'Sai': 25}
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}

fruits={'Orange':30,'Apple':80,'Mango':100,'Watermelon':40,'Kiwi':400,'Grape':35}
fruits.pop('Mango') #Delete and return from a key here 100 
