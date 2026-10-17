arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
arr[1], arr[2] = map(int, input().split())

for i in range(3, 11):
    arr[i] = (arr[i-2] + arr[i-1]) % 10

for i in range(1, 11):
    print(arr[i], end = " ")

