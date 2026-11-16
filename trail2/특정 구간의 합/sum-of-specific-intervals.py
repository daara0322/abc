n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code 
def f(x, y):
    sum_val = 0
    for i in range(x-1, y):
        sum_val += arr[i]
    return sum_val

def g(a) :
    for i in range(m) :
        x = queries[i][0]
        y = queries[i][1]
        print(f(x, y))
    
g(m)