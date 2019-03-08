import copy
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]
     ]
c = copy.deepcopy(a)

for i in range(len(a)):
    for j in range(len(c)):
        c[i][j] = a[j][i]

print(a)
print(c)
