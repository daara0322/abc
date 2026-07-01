arr = list(map(int, input().split()))

for i in range(10):
    new = (arr[i] + arr[i+1]) % 10
    arr.append(new)
    print(arr[i], end=" ")