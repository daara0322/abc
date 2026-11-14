n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def fun(x) :
    for i in range(n):
        if arr[i] < 0 :
            arr[i] = -arr[i]
    return

fun(arr)

for i in arr :
    print(i, end=' ')