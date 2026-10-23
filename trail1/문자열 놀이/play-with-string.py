s, q = tuple(input().split())
q = int(q)
sarr = list(s)

for _ in range(q):
    arr = input().split() 
    if arr[0] == '1':
        a = int(arr[1])
        b = int(arr[2])
        temp = sarr[a-1]
        sarr[a-1] = sarr[b-1]
        sarr[b-1] = temp

        joarr = ''.join(sarr)
        print(joarr)

    else :
        for i in range(len(sarr)):
            if sarr[i] == arr[1]:
                sarr[i] = arr[2]
        joarr = ''.join(sarr)
        print(joarr)
    

