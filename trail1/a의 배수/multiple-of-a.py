n, a = map(int, input().split())
i = 1
while n >= 1 :
    if i % a == 0 :
        print(1)
    else :
        print(0) 
    n -= 1
    i += 1