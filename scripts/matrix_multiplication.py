# 3 X 3
x = [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]
     ]

# 3 X 2
y = [[1, 2],
     [1, 2],
     [1, 2]
     ]

# Output : 3 X 2 Matrix

z = [[0, 0],
     [0, 0],
     [0, 0]]

for i in range(len(x)):
     for j in range(len(y[0])):
          for k in range(len(y)):
               z[i][j] += x[i][k] * y[k][j]

for x in z:
     print(x)
