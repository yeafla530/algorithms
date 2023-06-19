DOT = 10**9
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def is_possible(dist):
    cnt = 1
    last_idx = 0

    for i in range(1, n):
        if arr[i] - arr[last_idx] >= dist:
            cnt += 1
            last_idx = i

    # 
    return cnt >= m

# 가장 인접한 두 물건의 최대
arr.sort()
left = 1 # 답이 될 수 있는 가장 작은 숫자
right = DOT # 답이 될 수 있는 가장 큰 숫자
ans = 0

while left <= right:
    # 고정되어있는 거리
    mid = (left + right) // 2

    if is_possible(mid):
        left = mid + 1
        ans = max(ans, mid)
    
    else:
        right = mid - 1

print(ans)