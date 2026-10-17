arr = list(map(int, input().split()))

for i in range(2, 10):
    new = arr[i-1] + 2*arr[i-2]
    arr.append(new)

for i in arr:
    print(i, end=" ")