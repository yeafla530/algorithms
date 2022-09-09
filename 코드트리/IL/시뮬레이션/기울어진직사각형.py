n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_score(x, y, k, l):
    score = 0
    dxs = [-1, -1, 1, 1]
    dys = [1, -1, -1, 1]
    move_nums = [k, l, k, l]

    for (dx, dy, move_num) in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x = x + dx
            y = y + dy 

            if not in_range(x, y):
                return 0
            
            score += a[x][y]
    
    return score


max_ans = 0
# 대각선 시작하는 위치 (i, j)
for i in range(n):
    for j in range(n):
        # 너비 높이 : (k, l)
        for k in range(1, n):
            for l in range(1, n):
                max_ans = max(max_ans, get_score(i, j, k, l))
            
print(max_ans)