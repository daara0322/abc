c, n = input().split()
n = int(n)

if c == "A" :
    for i in range(n) :
        print(i+1, end=" ")
elif c == "D" :
    while n >= 1 :
        print(n, end=" ")
        n-=1