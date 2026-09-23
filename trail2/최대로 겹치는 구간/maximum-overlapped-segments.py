n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
OFFSET = 100
MAX_R = 200
checked = [0] * (MAX_R +1)
for a, b in segments :
    a, b = a+OFFSET, b+OFFSET
    for i in range(a, b):
        checked[i] += 1

print(max(checked)) 