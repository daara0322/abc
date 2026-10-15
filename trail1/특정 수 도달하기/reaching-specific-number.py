arr = list(map(int, input().split()))
sum_val = 0
for i in range(len(arr)):
    if arr[i] >= 250 :
        sum_val = sum(arr[0:i])
        print(sum_val, round(sum_val/i, 1))
        break
if sum_val == 0 :
    print(sum(arr), round(sum(arr)/10, 1))