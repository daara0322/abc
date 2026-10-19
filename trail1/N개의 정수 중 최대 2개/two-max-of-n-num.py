import sys
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
arr_new = []
for _ in range(n):
    max_val = -sys.maxsize
    for elem in a :
        if elem > max_val :
            max_val = elem
    arr_new.append(max_val)
    a.remove(max_val)  
for i in range(0, 2):
    print(arr_new[i], end=" ")  