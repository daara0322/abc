n = int(input())
arr = list(map(int, input().split()))
cnt = 0
a = 0
for i in range(n):
    if arr[i] == 2 :
        cnt += 1
    if cnt == 3 :
        a = i
        break

print(a+1)