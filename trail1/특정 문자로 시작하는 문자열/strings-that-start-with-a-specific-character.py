n = int(input())
arr = [input() for _ in range(n)]
a = input()
cnt = 0 
sum_val = 0

for i in range(n) :
    if arr[i][0] == a :
        cnt+=1
        sum_val += len(arr[i])

mean_val = sum_val/cnt
print(cnt, f"{mean_val:.2f}")