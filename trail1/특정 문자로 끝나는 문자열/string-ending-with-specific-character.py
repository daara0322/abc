arr = [input() for _ in range(11)]
a = arr[10]
cnt = 0
for i in range(10) :
    b = len(arr[i])
    if arr[i][b-1] == a :
        print(arr[i])
        cnt += 1

if cnt == 0 :
    print("None")