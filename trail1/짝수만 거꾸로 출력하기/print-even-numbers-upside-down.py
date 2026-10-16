n = int(input())
arr = list(map(int, input().split()))
arr_lis = []
for i in arr:
    if i % 2 ==0:
        arr_lis.append(i)
for i in range(len(arr_lis)):
    print(arr_lis[len(arr_lis)-1-i], end=' ') 