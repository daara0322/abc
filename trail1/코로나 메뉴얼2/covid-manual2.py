A, B, C, D = 0, 0, 0, 0
for _ in range(3):
    a, b = input().split()
    b = int(b)
    if a == 'Y' and b >= 37 :
        A += 1
    elif a == 'N' and b >= 37:
        B += 1
    elif a == 'Y' and b < 37:
        C += 1
    else :
        D += 1

print(A, B, C, D, end=" ")
if A >= 2:
    print("E")