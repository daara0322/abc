n = int(input())
cnt = 64

for i in range(n):
    for j in range(n):
        if chr(cnt) == 'Z':
            cnt = 64
        if i>j :
            print(" ", end=' ')
        else :
            print(chr(cnt+1), end=" ")
            cnt+=1
    print()
