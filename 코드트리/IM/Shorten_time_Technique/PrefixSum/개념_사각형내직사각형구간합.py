arr = [
    [0, 0, 0, 0],
    [0, 1, 2, 3],
    [0, 3, 6, 2],
    [0, 7, 5, 5]
]
prefix_sum = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for i in range(1, 4):
    for j in range(1, 4):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + prefix_sum[i-1][j-1] + arr[i][j]


# 1,1 ~ 3,3
print(prefix_sum[3][3] - prefix_sum[0][3] - prefix_sum[3][0] + prefix_sum[0][0])
# 1,2 ~ 3,2
print(prefix_sum[3][2] - - prefix_sum[0][2] - prefix_sum[3][1] + prefix_sum[0][1])