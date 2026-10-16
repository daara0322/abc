arr =  list(map(int, input().split()))
arr_lis = []

for i in arr:
    if i == 0:
        break
    arr_lis.append(i)

arr_sum = sum(arr_lis)
arr_len = len(arr_lis)
arr_mean = round(arr_sum / arr_len, 1)

print(arr_sum, arr_mean)