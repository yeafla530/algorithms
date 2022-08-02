from collections import deque
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def bfs(rows, columns, max_virus, queries, answer):
    queue = deque()
    idx = 0
    queue.append((queries[idx][0] - 1, queries[idx][1] - 1))
    

    while len(queue):
        print(queue)
        r, c = queue.popleft()
        answer[r][c] += 1
        if answer[r][c] <= max_virus:
            # print('first', queries[idx][0] - 1, queries[idx][1] - 1)
            if (len(queue) == 0 and idx != len(queries)-1):
                idx += 1
                queue.append((queries[idx][0] - 1, queries[idx][1] - 1))
        
        elif answer[r][c] > max_virus:            
            for j in range(4):
                x = c + dx[j]
                y = r + dy[j]
                
                # print('xy', x, y)
                if (0 <= x < columns and 0 <= y < rows and answer[y][x] <= max_virus):
                    queue.append((y, x))
         
                    # if (answer[y][x] == max_virus):
                        # print('yx', y, x)
                    # else:
                        # answer[y][x] += 1
                        # print(queries[idx][0] - 1, queries[idx][1] - 1)
                        # if (idx != len(queries)-1):
                        #     queue.append((queries[idx][0] - 1, queries[idx][1] - 1))
                        #     idx += 1
        
        print(idx, r, c, answer)

    return answer


def solution(rows, columns, max_virus, queries):
    answer = [[0]*columns for _ in range(rows) ]

    return bfs(rows, columns, max_virus, queries, answer)










solution(3, 4, 2, [[3, 2],[3, 2],[2, 2],[3, 2],[1, 4],[3, 2],[2, 3],[3, 1]])