n, a = tuple(input().split())
n = int(n)
arr = [input() for _ in range(n)]
cnt = 0

for elem in arr :
    if elem == a :
        cnt += 1

print(cnt)