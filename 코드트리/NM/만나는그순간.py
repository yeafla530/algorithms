n, m = map(int, input().split())
MAX_T = 1000000

pos_a = [0] * MAX_T
pos_b = [0] * MAX_T

# A가 매 초마다 서있는 위치를 기록
time_a = 1
for _ in range(n):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a-1] + (1 if d == 'R' else -1)
        time_a += 1
    
time_b = 1
for _ in range(m):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b-1] + (1 if d == 'R' else -1)
        time_b += 1

ans = -1
for i in range(1, time_a):
    if pos_a[i] == pos_b[i]:
        ans = i
        break

print(ans)