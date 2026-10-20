n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
a = 0
for i in range(n):
    a = a+1
    for j in range(n):
        arr[i][j] = a+j*n

for i in arr :
    for j in i :
        print(j, end=" ")
    print()

