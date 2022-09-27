arr = [0, 6, 3, 2, 4, 9, 1]
k = 10
n = 6

# 가능한 구간 중 최대 크기를 구합니다.
ans = 0

# 구간 잡기
sum_val = 0
j = 0

for i in range(1, n+1):
    # 그 다음 수가 영역을 넘지않고, 정래진 수보다 작을경우 
    while j + 1 <= n and sum_val + arr[j+1] <= k:
        sum_val += arr[j+1]
        j += 1
    
    ans = max(ans, j - i + 1)
    sum_val -= arr[i]

print(ans)
