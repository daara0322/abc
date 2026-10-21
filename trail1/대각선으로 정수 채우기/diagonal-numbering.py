n, m = map(int, input().split())

# Please write your code here.
# 0,0 = 1  
# 0,1 = 2 # 1,0 = 3 
# 0,2 = 4 # 1,1 = 5 # 2,0 = 6 
# 0,3 = 7 # 1,2 = 8 # 2,1 = 9 # 3,0 
# 3, 5 ..


arr = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1

for k in range(n + m - 1):
    for i in range(n):
        j = k - i

        if 0 <= j < m:
            arr[i][j] = cnt
            cnt += 1

for elem in arr :
    for i in elem :
        print(i, end=" ")
    print()
        
