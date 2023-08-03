n = int(input())
arr = list(map(int, input().split()))

# O(n^2)이면 안된다
# 그리디하게 
# [0, 1, 2, 3]위치
next = [[-1, -1, -1, -1] for _ in range(n+1)]

# 맨 끝에서부터 가장 가까운 1, 2, 3 위치 구하기
for i in range(n-1, -1, -1):
    next[i] = next[i+1][:]
    if i + 1 < n:
        next[i][a[i+1]] = i + 1

# 가장 가까운 1, 2, 3위치를 구한다
# 가장 먼 위치를 구한다
cur, cnt = 0, 0
while cur != n-1:
    cur = max(next[cur])
    cnt += 1

print(cnt)