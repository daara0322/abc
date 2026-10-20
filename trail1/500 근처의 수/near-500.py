arr = list(map(int, input().split()))
min_val = 1000
max_val = 0
for elem in arr :
    if elem < 500 :
        if elem > max_val :
            max_val = elem
    else :
        if elem < min_val :
            min_val = elem

print(max_val, min_val)

