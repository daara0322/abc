arr = input().split()
brr = input().split()
crr = input().split()
aS = arr[0]
ao = int(arr[1])
bS = brr[0]
bo = int(brr[1])
cS = crr[0]
co = int(crr[1])
sum = 0

if aS == 'Y' and ao >= 37 :
    sum += 1
if bS == 'Y' and bo >= 37 :
    sum+=1
if cS == 'Y' and co >= 37 :
    sum+=1

if sum >=2 :
    print("E")
else :
    print("N")
