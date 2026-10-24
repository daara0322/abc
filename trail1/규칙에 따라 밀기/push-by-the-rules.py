A = input()
B = input()


for i in range(len(B)):

    if B[i] == "L":
        A = A[1:] + A[0]

    else :
        A = A[-1] + A[:-1]

print(A)