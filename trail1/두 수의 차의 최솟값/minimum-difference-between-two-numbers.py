n = int(input())
arr = list(map(int, input().split()))
min_val = 100
for i in range(n) :
    for j in range(n) :
        if i == j :
            continue
        elif abs(arr[i] - arr[j]) < min_val :
            min_val = abs(arr[i]-arr[j])

print(min_val)