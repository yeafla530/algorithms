n, m = map(int, input().split())
MAX_DIS = 1000000
pos_a = [0 for _ in range(MAX_DIS + 1)]
# pos_a = [0 for _ in range(20)]
pos_b = [0 for _ in range(MAX_DIS + 1)]
# pos_b = [0 for _ in range(20)]

time_a = 1
for _ in range(n):
    v, t = map(int, input().split())
    # 1시간마다 얼마나 이동했는지 체크
    for _ in range(time_a, t+time_a):
        pos_a[time_a] = pos_a[time_a - 1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(time_b, time_b+t):
        pos_b[time_b] = pos_b[time_b - 1] + v
        time_b += 1
    
# A와 B 중 더 앞서 있는 경우를 확인합니다.
# A가 리더면 1, B가 리더면 2로 관리합니다.
leader, ans = 0, 0
for i in range(1, time_a):
    if pos_a[i] > pos_b[i]:
        if leader == 2:
            ans += 1
        leader = 1
    elif pos_a[i] < pos_b[i]:
        if leader == 1:
            ans += 1
        leader = 2

print(ans)