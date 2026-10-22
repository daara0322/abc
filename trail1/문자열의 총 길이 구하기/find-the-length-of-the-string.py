arr = input().split()
sum_val = 0

for i in range(len(arr)):
    sum_val += len(arr[i])

print(sum_val)