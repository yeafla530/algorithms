def solution(board):
    answer = 0
    n = len(board)
    safe_area = [[0 for _ in range(n)] for _ in range(n)]
    
    dxs = [0, 1, 1, 1, 0, -1, -1, -1]
    dys = [1, 1, 0, -1, -1, -1, 0, 1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                safe_area[i][j] = 1
                for (dx, dy) in zip(dxs, dys):
                    nx = i + dx
                    ny = j + dy
                    
                    if 0 <= nx < n and 0 <= ny < n:
                        safe_area[nx][ny] = 1
            
    
    for i in range(n):
        for j in range(n):
            if safe_area[i][j] == 0:
                answer += 1
    return answer