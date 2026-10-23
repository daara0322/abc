n = int(input())
arr = input().split()
st = "".join(arr)

for i in range(len(st)):
    if (i+1)%5 == 0 :
        print(st[i], end="")
        print()
    else :
        print(st[i], end="")

