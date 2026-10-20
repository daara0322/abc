arr = [list(map(int, input().split())) 
        for _ in range(2)]
for i in range(2):
    mean_val = sum(arr[i][:])/4
    print(f"{mean_val:.1f}", end=" ")
print()
for j in range(4):
    mean_val = (arr[0][j]+arr[1][j])/2 
    print(f"{mean_val:.1f}", end=" ")
print()

print(f"{(sum(arr[0])+sum(arr[1]))/8:.1f}")
