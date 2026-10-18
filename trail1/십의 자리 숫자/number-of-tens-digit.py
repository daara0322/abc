arr = list(map(int, input().split()))
arr_new = [0]*9

for i in arr :
    if i == 0:
        break
    n = i//10
    if n == 0:
        continue
    arr_new[n-1] = arr_new[n-1] + 1

for i in range(len(arr_new)) :
    print(f"{i+1} - {arr_new[i]}")

