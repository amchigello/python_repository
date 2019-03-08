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
