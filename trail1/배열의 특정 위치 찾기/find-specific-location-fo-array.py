arr = list(map(int, input().split()))
arr_2sum = 0
arr_3sum = 0
for i in range(1, 10, 2):
    arr_2sum += arr[i]
for i in range(2, 10, 3):
    arr_3sum += arr[i]

print(f"{arr_2sum} {(arr_3sum/3):.1f}")
