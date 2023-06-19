# 주어진 그래프가 이분 그래프인가?


import sys
from collections import deque

si = sys.stdin.readline
n, m = map(int, si().split())
con = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, si().split())
    con[x].append(y)
    con[y].append(x)

color = [0 for _ in range(n+1)] # color[i] := i번 정점의 색깔. 0 (Unknown), 1 (Red), 2 (Blue)


def BFS(x):
    q = deque()
    q.append(x)
    color[x] = 1

    while q:
        x = q.popleft()
        for y in con[x]:
            if color[y] == 0:
                q.append(y)
                color[y] = 3 - color[x]



for i in range(1, n+1):
    if color[i] == 0:
        BFS(i)


print(color)
flag = True
for i in range(1, n+1):
    for j in con[i]:
        if color[i] == color[j]:
            flag = False

print(1 if flag else 0)

'''
7 8
1 2
1 6
2 4
2 3
3 5
4 5
5 7
6 7
=>
[0, 1, 2, 1, 1, 2, 2, 1]
1

'''