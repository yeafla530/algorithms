def dfs(x, y):
    global people_num
    for dx, dy in zip(dxs, dys):
        nx = x + dx 
        ny = y + dy

        if can_go(nx, ny):
            visited[nx][ny] = 1
            people_num += 1
            dfs(nx, ny)


visited[0][0] = 1
dfs(0, 0)