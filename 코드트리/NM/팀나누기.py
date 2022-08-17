
num = [1, 5, 6, 3]

def get_diff(i, j):
    sum1 = num[i] + num[j]
    sum2 = sum(num) - sum1
    return abs(sum1 - sum2)

min_diff = 100
for i in range(0, 4):
    for j in range(i+1, 4):
        min_diff = min(min_diff, get_diff(i, j))

print(min_diff)