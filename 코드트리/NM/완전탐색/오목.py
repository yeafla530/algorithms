arr = [list(map(int, input().split())) for _ in range(19)]
n = len(arr)
# 가로 확인

dxs = [1, 0, -1, 0, -1, 1, -1, 1]
dys = [0, 1, 0, -1, -1, 1, 1, -1]
is_finish = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for x in range(n):
    for y in range(n):
        
        ball = 0
        fx, fy = 0, 0
        if arr[x][y] == 1:
            ball = 1
            for k in range(8):
                count = 0
                for p in range(5):
                    nx = x + dxs[k] * p
                    ny = y + dys[k] * p

                    if in_range(nx, ny) and arr[nx][ny] == ball:
                        count += 1
                        if count == 3:
                            fx = nx
                            fy = ny

                if count == 5:
                    is_finish = True
                    break
            if is_finish:
                break

        elif arr[x][y] == 2:
            ball = 2
            for k in range(8):
                count = 0
                for p in range(5):
                    nx = x + dxs[k] * p
                    ny = y + dys[k] * p

                    if in_range(nx, ny) and arr[nx][ny] == ball:
                        count += 1
                        if count == 3:
                            fx = nx
                            fy = ny

                if count == 5:
                    is_finish = True
                    break
            if is_finish:
                break
        if is_finish:
            break
    if is_finish:
        break

print(ball)
if ball != 0:
    print(fx+1, fy+1)



# 답 
import sys
arr = [list(map(int, input().split())) for _ in range(19)]
n = len(arr)
# 가로 확인

dxs = [1, 0, -1, 0, -1, 1, -1, 1]
dys = [0, 1, 0, -1, -1, 1, 1, -1]
is_finish = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            continue
        for dx, dy in zip(dxs, dys):
            curt = 1
            curx = i
            cury = j

            while True:
                nx = curx + dx
                ny = cury + dy
                if in_range(nx, ny) == False:
                    break
                
                if arr[nx][ny] != arr[i][j]:
                    break
                curt += 1
                curx = nx
                cury = ny
            if curt == 5:
                print(arr[i][j])
                print(i + 2 * dx + 1, j + 2 * dy + 1)
                sys.exit()

print(0)

      