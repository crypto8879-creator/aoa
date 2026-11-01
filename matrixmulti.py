A = [[1, 2], 
     [3, 4]]

B = [[1, 2], 
     [3, 4]]


result = [[0, 0], 
          [0, 0]]


for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]

print("Standard 2x2 Result:")
for row in result:
    print(row)