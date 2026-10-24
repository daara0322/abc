A = input()
B = input()

# Please write your code here.
cnt = 0
while True :
    if B in A :
        n = A.index(B)
        A = A[:n] + A[n+len(B):]
    else :
        print(A)
        break
