n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
# Please write your code here
cnt = 0
for i in range(m) :
    for j in range(n):
        if i % 2 == 0:
            arr[j][i] = cnt
            cnt += 1
        else :
            arr[n-j-1][i] = cnt
            cnt += 1
for a in arr :
    for elem in a :
        print(elem, end =" ")
    print()
        