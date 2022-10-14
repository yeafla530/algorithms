n = int(input())
d = {}
graph = [[0]*n for _ in range(n)]
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
result = 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _ in range(n*n):
    arr = list(map(int, input().split()))
    d[arr[0]] = arr[1:]

    x, y = 0, 0
    max_cnt = 0
    no_f_cnt = 0
    dir_arr = []
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                continue
            friend_count = 0
            no_friend = 0

            for dx, dy in zip(dxs, dys):
                nx = i + dx
                ny = j + dy
                if in_range(nx, ny) and graph[nx][ny] in d[arr[0]]:
                    friend_count += 1

                if in_range(nx, ny) and graph[nx][ny] == 0:
                    no_friend += 1
            if max_cnt < friend_count:
                max_cnt = friend_count
                dir_arr = [(i, j, no_friend)]
                x, y = i, j

            elif max_cnt == friend_count:
                dir_arr.append((i, j, no_friend))

    # 1. 격자를 벗어나지 않는 4방향 중 좋아하는 친구수 가장 많은 위치
    # 2. 비어있는 칸의 수가 가장 많은 위치
    # 3. 행번호가 가장 작은 위치
    # 4. 열번호가 가장 작은 위치
    dir_arr.sort(key=lambda x: -x[2])
    x, y, no_f_cnt = dir_arr[0]
    graph[x][y] = arr[0]

def get_score():
    score = 0
    for i in range(n):
        for j in range(n):
            count_friend = 0
            for dx, dy in zip(dxs, dys):
                nx = i + dx
                ny = j + dy

                if in_range(nx, ny) and graph[nx][ny] in d[graph[i][j]]:
                    count_friend += 1


            if count_friend > 0:
                score += 10 ** (count_friend - 1)
    return score

result = get_score()
print(result)