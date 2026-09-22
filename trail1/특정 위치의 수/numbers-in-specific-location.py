arr = input().split()
sum = 0
arr1 = []
arr1.append(int(arr[2]))
arr1.append(int(arr[4]))
arr1.append(int(arr[9]))

for i in range(3) :
    sum += arr1[i]
print(sum)
