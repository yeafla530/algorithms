# 그리디
n = int(input())
arr = list(map(int, input().split()))
next = [[-1, -1, -1, -1] for _ in range(n+1)] # next[i][k] = i번째 원소에서 오른쪽으로 가장 가까운 k값의 위치

# 가장 가까운 1, 2, 3을 찾고
# 그중 제일 먼 곳으로 이동


# 만약 next[i][k] = -1이라면, i번째 원소의 오른쪽에는 더이상 k가 등장하지 않는다
# next 배열 계산
for i in range(n-1, -1, -1): # 이번에 nxt[i]를 계산할 차례
    next[i] = next[i+1][:] # i+1번 원소의 next정보를 계승
    if i + 1 < n:
        next[i][arr[i+1]] = i + 1

print(next)
# greedy하게 이동
cur, cnt = 0, 0
# 다음에 이동할 위치는 현재 위치에서 이동할 수 있는 다음 1, 2, 3
while cur != n-1:
    cur = max(next[cur])    # 현재 위치(cur)에서 갈 수 있는 1, 2, 3위치들 중 
    cnt += 1                # 가장 먼 곳으로 이동


print(cnt)

'''
6
1 2 2 2 1 3
=> 1

5 
1 2 1 3 3
=> 2
'''