n = int(input())

for i in range(0, 2*n, 2):
    for j in range(11+i, 11+2*n+i, 2):
        print(j, end=' ')
    print()