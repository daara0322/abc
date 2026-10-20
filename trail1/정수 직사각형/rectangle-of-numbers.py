n, m = map(int, input().split())

arr_2 = [[0 for _ in range(m)] for _ in range(n)]
a = 1
for i in range(n):
    for j in range(m):
        arr_2[i][j] = a
        a += 1

for arr in arr_2:
    for elem in arr :
        print(elem, end=" ")
    print()