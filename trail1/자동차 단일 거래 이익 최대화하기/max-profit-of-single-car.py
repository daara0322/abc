n = int(input())
price = list(map(int, input().split()))
max_val = 0
# Please write your code here.
for i in range(n) :
    for j in range(i+1, n):
        if (price[j] - price[i]) > max_val :
            max_val = price[j] - price[i]

print(max_val)
