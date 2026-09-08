A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

print("Addition")

for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[i][j]+B[i][j])
    print(row)

print("\nTranspose")

for i in range(2):
    row=[]
    for j in range(2):
        row.append(A[j][i])
    print(row)

print("\nRow Sum")

for row in A:
    print(sum(row))

print("\nColumn Sum")

for j in range(2):
    total=0
    for i in range(2):
        total+=A[i][j]
    print(total)