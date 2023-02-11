# 내 풀이
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

happy = 0

for i in range(n):
    base = grid[i][0]
    count = 1
    max_cnt = 1
    for j in range(1, n):
        if base == grid[i][j]:
            count += 1
        else:
            count = 1
            base = grid[i][j]

        max_cnt = max(count, max_cnt)

    if max_cnt >= m:
        happy += 1

for i in range(n):
    base = grid[0][i]
    count = 1
    max_cnt = 1
    for j in range(1, n):
        if base == grid[j][i]:
            count += 1
        
        else:
            count = 1
            base = grid[j][i]

        max_cnt = max(count, max_cnt)
    if max_cnt >= m:
        happy += 1

print(happy)


# 해설
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
seq = [0 for _ in range(n)]

def is_happy_seq():
    consecutive_count, max_cnt = 1, 1
    for i in range(1, n):
        if seq[i-1] == seq[i]:
            consecutive_count += 1
        
        else:
            consecutive_count = 1
        max_cnt = max(max_cnt, consecutive_count)

    return max_cnt >= m




num_happy = 0

for i in range(n):
    seq = grid[i][:]

    if is_happy_seq():
        num_happy += 1

for j in range(n):
    for i in range(n):
        seq[i] = grid[i][j]
    
    if is_happy_seq():
        num_happy += 1

print(num_happy)