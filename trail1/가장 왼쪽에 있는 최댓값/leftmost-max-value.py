n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
while True :
    max_val = -1
    for i in range(n) :
        if max_val < a[i] :
            max_val = a[i]

    print(a.index(max_val)+1, end=" ")
    n = a.index(max_val)
    if n == 0 :
        break
