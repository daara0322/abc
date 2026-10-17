n = int(input())
n1 = n
cnt = 0
while True :
    if cnt == 2:
        break
    print(n, end=' ')
    if n % 5 == 0:
        cnt += 1
    n = n+n1
    