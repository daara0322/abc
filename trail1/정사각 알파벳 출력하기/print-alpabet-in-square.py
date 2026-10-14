n = int(input())
cnt = 64

for _ in range(n):
    for _ in range(n):
        print(chr(cnt+1),end='')
        cnt+=1
    print()
