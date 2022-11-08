# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 0 = 없음
# 1 = 있음
# 2 = 장애인석

# 같은 구역에 속한 두 주차 칸 사이에 항상 상태가 1인 칸을 거치지 않고 이동하는 경로 존재
# 서로 다른 구역에 속한 두 주차 칸 사이에 주차구역 나눔
# 주차구역에 존재하는 상태가 0인 칸의 개수마다 1점 더함
# 상태가 2인 칸의 개수마다 2점을 뺀다
# 모든 주차구역에 대한 점수 측정하고 가장높은 점수를 가지고 있는 구역으로 차를 안내한다

# 주차구역이 존재하지 않고나 음수인 경우에는 0 출력
from collections import deque 

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
q = deque()
scores = []


dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]


def bfs():
	count = 0 
	while q:
		# print(q)
		x, y = q.popleft()
		visited[x][y] = 1
		if graph[x][y] == 0:
			count += 1
		elif graph[x][y] == 2:
			count -= 2
		
		# print("count", count)
		for dx, dy in zip(dxs, dys):
			nx = x + dx
			ny = y + dy
			if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and (graph[nx][ny] == 0 or graph[nx][ny] == 2):
				# print(nx, ny)
				q.append((nx, ny))
				visited[nx][ny] = 1
# 			
	
	# print("+++++++++++++++")
	# print(visited, count)
	scores.append(count)

for i in range(n):
	for j in range(m):
		if not visited[i][j] and (graph[i][j] == 0 or graph[i][j] == 2):
			visited[i][j] = 1
			q.append((i, j))
			bfs()


if len(scores) and max(scores) > 0:
	print(max(scores))

else:
	print(0)