N, Q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(Q):
    q_arr = list(map(int, input().split()))
    if q_arr[0] == 3:
        for i in range(q_arr[1], q_arr[2]+1):
            print(arr[i-1], end=" ")
        print()
    elif q_arr[0] == 1:
        print(arr[q_arr[1]-1])
    elif q_arr[0] == 2:
        if q_arr[1] in arr:
            print(arr.index(q_arr[1])+1)
        else :
            print(0)


    

