n = int(input())

for i in range(n):
    for j in range(n):
        if j%2 == 0 :
            print(i+1, end='')
        else :
            print(n-i, end='')
    print()
""" 
0 0 > 1
1 0 > 2
2 0 > 3
3 0 > 4

0 1 > 4
1 1 > 3
2 1 > 2
3 1 > 1

0 2 > 1
1 2 > 2
2 2 > 3
3 2 > 4
"""