n = int(input())
cnt = 64
for i in range(n):
    for j in range(i+1):
        if chr(cnt) == 'Z':
            cnt = 64
        print(chr(cnt+1), end='')
        cnt+=1
    print()
