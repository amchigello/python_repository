import collections

name = 'Panduranga'
fruits = ['Apple', 'Orange', 'Banana', 'Grapes', 'Grapes', 'Grapes', 'Apple']

print(dict(collections.Counter(name)))
print(dict(collections.Counter(fruits)))

y={}
for x in name:
    if x in y:
        y[x]+=1
    else:
        y[x]=1

print(y)