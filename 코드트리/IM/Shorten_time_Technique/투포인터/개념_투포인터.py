arr = [0, 6, 3, 2, 4, 9, 1]
k = 10
n = 6

# 가능한 구간 중 최대 크기를 구합니다.
ans = 0
# 구간 합
sum_val = 0
j = 0
for i in range(1, n+1):
    while j + 1 <= n and sum_val + arr[j+1] <= k:
        sum_val += arr[j+1]
        j += 1
    
    ans = max(ans, j - i + 1)

    sum_val -= arr[i]

print(ans)
