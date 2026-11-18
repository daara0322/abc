n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()
bo = True


for i in range(n):
    if A[i] != B[i] :
        bo = False
    
if bo :
    print('Yes')
else :
    print('No')