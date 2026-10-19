import sys
arr = list(map(int, input().split()))
arr_new = []

for elem in arr :
    if elem == 999 or elem == -999:
        break
    arr_new.append(elem)

min_val = sys.maxsize
max_val = -sys.maxsize
for elem in arr_new :
    if elem > max_val :
        max_val = elem
    if elem < min_val :
        min_val = elem

print(max_val, min_val)
