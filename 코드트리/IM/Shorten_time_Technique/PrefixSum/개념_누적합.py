arr = [0, 3, 6, 2, 6, 7, 7, 2]
prefix_sum = [0] * 8

prefix_sum[0] = 0

for i in range(1, 8):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

# [2, 5] 까지 합 = 21
print(prefix_sum[5] - prefix_sum[1])
# [0, 5] 까지 합 = 24
print(prefix_sum[5] - prefix_sum[0])