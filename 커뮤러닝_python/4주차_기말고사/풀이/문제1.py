def solution(rows, columns, max_virus, queries):
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    def dfs(x, y):
        if x >= rows or x < 0 or y >= columns or y < 0 or visit[x][y]:
            return
        
        visit[x][y] = 1
        if matrix[x][y] < max_virus:
            matrix[x][y] += 1
        else:
            dfs(x-1, y)
            print('b1', visit)
            dfs(x+1, y)
            print('b2', visit)
            dfs(x, y-1)
            print('b3', visit)
            dfs(x, y+1)
            print('b4', visit)

        print('a', matrix, x, y)
        print('b', visit)

    

    for x, y in queries:
        visit = [[0 for _ in range(columns)] for _ in range(rows)]
        dfs(x-1, y-1)
    return matrix

solution(3, 4, 2, [[3, 2],[3, 2],[2, 2],[3, 2],[1, 4],[3, 2],[2, 3],[3, 1]])