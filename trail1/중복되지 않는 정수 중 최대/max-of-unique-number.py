import sys
n = int(input())
nums = list(map(int, input().split()))
# Please write your code here.

for _ in range(n):
    max_val = -sys.maxsize
    for elem in nums :
        if max_val < elem :
            max_val = elem
    cnt = 0
    for elem in nums :
        if max_val == elem :
            cnt += 1

    if cnt >= 2:
        for _ in range(cnt):
            nums.remove(max_val)
    else : 
        break

if cnt == 0 :
    print(-1)
elif cnt == 1:
    print(max_val)

