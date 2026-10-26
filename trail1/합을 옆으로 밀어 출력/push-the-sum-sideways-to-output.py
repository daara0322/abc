n = int(input())
arr = [int(input()) for _ in range(n)]
sum_arr = sum(arr)
str_sum = str(sum_arr)

str_sum = str_sum[1] + str_sum[2:] + str_sum[0]
print(str_sum)