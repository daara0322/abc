n = int(input())
arr = [input() for _ in range(n)]
cnt = 0
sum_val = 0
for i in range(n):
    sum_val += len(arr[i])
    if arr[i][0] == 'a' :
        cnt += 1
print(sum_val, cnt)