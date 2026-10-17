arr_new = [0]*6
arr = list(map(int, input().split()))

for i in arr :
    arr_new[i-1] += 1

for i in range(6) :
    print(f"{i+1} - {arr_new[i]}")
    