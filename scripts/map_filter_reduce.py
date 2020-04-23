from functools import reduce
import statistics
temp = [('Bangalore', 34), ('Mysore', 34), ('Bangalore', 30), ('Chennai', 40), ('Manali', 22),
        ('Mumbai', 38), ('Mangalore', 37), ('Kolkata', 32), ('Delhi', 42)]
avg = statistics.mean([x[1] for x in temp])
print(avg)

print("Use of filter")
greater_than_avg = filter(lambda x: x[1] > avg, temp)
print(list(greater_than_avg))

print("Use of Map")
categorical_temp = map(
    lambda x: x[0]+" is Hot" if x[1] > avg else x[0]+" is Not Hot", temp)
print(list(categorical_temp))

x = [1, 2, 3, 4, 5]
print("Use of reduce")
print(x)
print(reduce(lambda x, y: x+y+1, x))
