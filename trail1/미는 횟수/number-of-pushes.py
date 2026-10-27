A = input()
B = input()
n = 0 
A_st = A

while True :
    if  A == B :
        print(n)
        break
    A = A[-1] + A[:-1]
    n += 1
    if A == A_st :
        print(-1)
        break
        