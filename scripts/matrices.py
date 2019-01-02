a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

b = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

c = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
 
print("Sum of matrices")   
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j] = a[i][j] + b[i][j]
        
print(c)        

print("Transpose matrices")

for i in range(len(a)):
    for j in range(len(b)):
        c[i][j] = a[j][i]
        
print(c)        
