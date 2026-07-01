z = int(input())
num = list(map(int, input().split()))


num_new = [new**2 for new in num]

for i in range(z):
    print(num_new[i], end=" ")