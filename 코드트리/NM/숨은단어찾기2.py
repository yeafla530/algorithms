n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

# 왼쪽부터 시계방향
dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [-1, -1, 0, 1, 1, 1, 0, -1]


# 가로, 세로, 대각선에서 LEE를 찾는다
cnt = 0

def in_range(nx, ny, mx, my):
    return 0 <= nx < n and 0 <= ny < m and 0 <= mx < n and 0 <= my < m
for x in range(n):
    for y in range(m):
        for k in range(4):
            nx = x + dxs[k]
            ny = y + dys[k]

            mk = k+4
            mx = x + dxs[mk]
            my = y + dys[mk]
            # if in_range(nx, ny, mx, my):
            #     print(arr[nx][ny], arr[x][y], arr[mx][my])
            if in_range(nx, ny, mx, my) and ((arr[nx][ny] == "L" and arr[x][y] == "E" and arr[mx][my] == "E") or (arr[mx][my] == "L" and arr[x][y] == "E" and arr[nx][ny] == "E")):
                cnt += 1



print(cnt)

## 풀이

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

# 왼쪽아래 대각선부터 반시계방향
dxs, dys = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]


# 가로, 세로, 대각선에서 LEE를 찾는다
cnt = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 모든 칸에 대해 해당칸이 L이면 주변 가로세로 대각선 인접한 8칸에 대해 완탐 진행
# break 조건 : 현재 방향으로 한칸 더 갓을 때 격자 벗어나거나 'E'가 아닌 다른 문자 있는 경우 
for i in range(n):
    for j in range(m):

        if arr[i][j] != "L":
            continue
        
        # 8방향 돈다
        for dx, dy in zip(dxs, dys):
            # 단어 개수
            curt = 1
            curx = i
            cury = j
            # 같은 방향으로 break될때까지 반복
            while True:
                nx = curx + dx
                ny = cury + dy 
                if not in_range(nx, ny) or arr[nx][ny] != "E":
                    break
                
                curt += 1
                curx = nx
                cury = ny
                if curt == 3:
                    break

            if curt >= 3:
                cnt += 1

print(cnt)