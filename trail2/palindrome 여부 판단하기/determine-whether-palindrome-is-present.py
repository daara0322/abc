A = input()

# Please write your code here.

def modify(A) :
    B = ""
    for i in range(len(A)-1, -1, -1):
        B += A[i]
    return B


new_A = modify(A)

if A == new_A :
    print("Yes")
else :
    print("No")