a, b = map(int, input().split())
ab_sum = str(a+b)
cnt = 0

for elem in ab_sum :
    if elem == '1' :
        cnt+= 1

print(cnt)