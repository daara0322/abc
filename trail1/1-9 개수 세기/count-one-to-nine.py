n = int(input())
arr = list(map(int, input().split()))
arrnew = [0] * 9

for i in arr :
    arrnew[i-1] = arrnew[i-1] + 1

for j in arrnew:
    print(j)
    