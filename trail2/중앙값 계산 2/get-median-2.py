n = int(input())
arr = list(map(int, input().split()))
newarr = []
# Please write your code here.

for i in range(n):
    newarr.append(arr[i])
    if i % 2 == 0 :
        new1arr = newarr 
        new1arr.sort()
        print(new1arr[i//2], end=' ')
    