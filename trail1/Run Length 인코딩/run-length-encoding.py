A = input()
arr = []
cnt = 1
arr.append(A[0])
if len(A) == 1 :
    arr.append('1')
# Please write your code here.
for i in range(1, len(A)):
    if A[i-1] == A[i] :
        cnt+=1
    else : 
        arr.append(str(cnt))
        arr.append(A[i])        
        cnt = 1
    if i == len(A)-1 :
        arr.append(str(cnt))

cnt = 0
for elem in arr:
    for i in elem :
        cnt+=1

print(cnt)
for elem in arr :
    for i in elem :
        print(i, end="")