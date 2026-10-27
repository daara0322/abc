n, m = map(int, input().split())

# Please write your code here.
def fun(n, m):
    cnt = 1
    while True :
        max_val = max(n, m)
        if (max_val * cnt) % min(n, m) == 0 :
            print(max_val*cnt)
            break
        cnt += 1

fun(n, m) 