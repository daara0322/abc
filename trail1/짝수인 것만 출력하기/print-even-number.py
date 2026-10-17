n = int(input())
arr = list(map(int, input().split()))
arr_new = []
for i in arr :
    if i%2 ==0:
        arr_new.append(i)

for i in arr_new :
    print(i, end=' ') 