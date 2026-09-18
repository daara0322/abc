arr = input().split()
brr = input().split()

aa = int(arr[0])
aS = arr[1]
bb = int(brr[0])
bS = brr[1]

if aa >= 19 and aS == 'M' or (bb >= 19 and bS == 'M') :
    print(1)
else :
    print(0)