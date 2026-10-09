a, b = map(int, input().split())
pond = 1

for i in range(a, b+1):
    pond *= i
print(pond)