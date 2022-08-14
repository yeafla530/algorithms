n, m = map(int, input().split())
MAX_T = 1000000
pos_a, pos_b = [0] * (MAX_T+1), [0] * (MAX_T+1)

time_a = 1
for _ in range(n):
    t, d = input().split()
    t = int(t)
    for i in range(time_a, time_a+t):
        if d == 'R':
            pos_a[i] = pos_a[i-1] + 1
        else:
            pos_a[i] = pos_a[i-1] - 1
        time_a += 1

time_b = 1
for _ in range(m):
    t, d = input().split()
    t = int(t)
    for i in range(time_b, time_b+t):
        if d == 'R':
            pos_b[i] = pos_b[i-1] + 1
        else:
            pos_b[i] = pos_b[i-1] - 1
        time_b += 1
# 종료한 이후에는 같은 위치에 계속 머물러 있으며
# 다른 로봇이 움직임에 따라 두 로봇이 같은 위치에 오게될 수 있습니다.
if time_a < time_b:
    for i in range(time_a, time_b):
        pos_a[i] = pos_a[i-1]
else:
    for i in range(time_b, time_a):
        pos_b[i] = pos_b[i-1]


time_max = max(time_a, time_b)
cnt =  0
for i in range(1, time_max):
    if pos_a[i] == pos_b[i] and pos_a[i - 1] != pos_b[i - 1]:
        cnt += 1

print(cnt)
        
