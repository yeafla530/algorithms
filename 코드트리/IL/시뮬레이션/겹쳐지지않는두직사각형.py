import sys
INT_MIN = -sys.maxsize

# 숫자들 총합을 최대로
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

board = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def check_board():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                return True
    return False

def draw(x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            board[i][j] += 1

def clear_both():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0

def overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_both()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)
    return check_board()

def rect_sum(x1, y1, x2, y2):
    score = 0
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            score += a[i][j]

    return score
    
def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = INT_MIN
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not overlapped(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum, rect_sum(x1, y1, x2, y2) + rect_sum(i, j, k, l))

    return max_sum


def find_max_sum():
    max_sum = INT_MIN
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    max_sum = max(max_sum, find_max_sum_with_rect(i, j, k, l))

    return max_sum


ans = find_max_sum()


print(ans)

