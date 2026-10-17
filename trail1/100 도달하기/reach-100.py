n = int(input())
arr = []
arr.append(1)
arr.append(n)

for i in range(2, 50):
    new = arr[i-1] + arr[i-2]
    arr.append(new)
    if new > 100 :
        break

for i in arr:
    print(i, end=' ') 