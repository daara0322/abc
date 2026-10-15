n = int(input())
arr = list(map(float, input().split()))

arr_sum = sum(arr)
arr_mean = round(arr_sum / n, 1)
print(arr_mean)

if arr_mean >= 4:
    print('Perfect')
elif arr_mean >= 3:
    print("Good")
elif arr_mean < 3:
    print("Poor")
