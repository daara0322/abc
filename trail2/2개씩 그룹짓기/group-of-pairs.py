n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

nums.sort()
lis = []

for i in range(2*n):
    lis.append(nums[2*n-1-i] + nums[i])

lis.sort()
print(lis[2*n-1])