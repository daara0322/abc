import sys
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = sys.maxsize
cnt = 0 
for elem in a :
    if elem < min_val :
        min_val = elem
    
for elem in a :
    if elem == min_val :
        cnt += 1

print(min_val, cnt)
