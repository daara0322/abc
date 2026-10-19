N1, N2 = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
arrnew = []
new = []
for i in range(len(arrA)) :
    if arrA[i] == arrB[0]:
        arrnew.append(i)

for i in arrnew :
    cnt = 0
    new = []
    for j in range(i, len(arrA)):
        if arrA[j] == arrB[cnt]:
            new.append(arrB[cnt])
            cnt+=1
        else : 
            break
        if cnt == len(arrB) :
            break
    if new == arrB :
        break
if new == arrB :
    print("Yes")
else :
    print("No")
