A, B = map(int, input().split())
sum_val = 0
arr = [0] * 10
while A > 1 :
    n = A%B 
    arr[n] = arr[n] + 1
    A = A//B
for i in range(len(arr)):
    sum_val = sum_val + arr[i]**2
print(sum_val)