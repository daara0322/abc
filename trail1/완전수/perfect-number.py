start, end = map(int, input().split())
result = 0
# Please write your code here.
for i in range(start, end+1):
    cnt = 0
    for j in range(1, i):
        if i%j == 0:
            cnt += j
    if cnt == i :
        result += 1
print(result)    

