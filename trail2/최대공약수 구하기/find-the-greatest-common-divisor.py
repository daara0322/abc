n, m = map(int, input().split())

# Please write your code here.
def fun(n, m) :
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0 and m%i == 0:
            cnt = i
    print(cnt)

fun(n, m)

            