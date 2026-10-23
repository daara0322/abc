st = input()
arr = list(st)
a = arr[0]
b = arr[1]
for i in range(len(arr)):
    if arr[i] == a:
        arr[i] = b
    elif arr[i] == b:
        arr[i] = a
st = "".join(arr)
print(st)