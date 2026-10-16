arr = list(map(int, input().split()))
arr_lis = []
for i in arr :
    if i == 0 :
        break
    arr_lis.append(i)
a = len(arr_lis)
for i in range(a):
    print(arr_lis[a-i-1], end=' ')
    