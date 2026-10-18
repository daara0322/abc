arr = list(map(int, input().split()))
arr_new = [0]*10

for i in arr :
    if i == 0:
        break
    i = i // 10 
    if i == 0:
        continue
    arr_new[i-1] = arr_new[i-1] + 1
a = 100
for i in range(len(arr_new)-1, -1, -1) :
    print(f"{a} - {arr_new[i]}")
    a -= 10