arr = list(map(int, input().split()))
arr2sum = 0
arr1sum = 0
n = len(arr)

for i in range(n) :
    if i % 2 == 0 :
        arr1sum += arr[i]
    else :
        arr2sum += arr[i]

if arr1sum > arr2sum :
    print(arr1sum - arr2sum)
elif arr2sum > arr1sum :
    print(arr2sum - arr1sum)
else :
    print(0)