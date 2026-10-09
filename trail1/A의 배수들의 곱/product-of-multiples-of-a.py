a, b = map(int, input().split())
pond = 1

for i in range(1, b+1):
    if i%a == 0:
        pond*=i 
print(pond)
        