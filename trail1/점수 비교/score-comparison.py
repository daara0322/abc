arr_0 = input().split()
arr_1 = input().split()

am = int(arr_0[0])
ae = int(arr_0[1])
bm = int(arr_1[0])
be = int(arr_1[1])

if am > bm and ae > be :
    print(1)
else :
    print(0)