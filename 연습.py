import sys
from collections import deque
si = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# 8방향 
dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
dist = [[[INF for _ in range(8)] for _ in range(m)] for _ in range(n)]

print(dist)
q = deque()
q.append((0, 0, 2)) # boot starts at (0, 0) and faces right side
dist[0][0][2] = 0

while q:
    x, y, d = q.popleft()
    # 
    for dd in [0, 1, 7]:
