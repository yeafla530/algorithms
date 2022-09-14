n = 4
m = 2
NONE = -1
graph = [list(map(int, input().split())) for _ in range(4)]
direction = input()
temp = [[0]*n for _ in range(n)]

# 시계방향 회전
def rotate():
    for i in range(n):
        for j in range(n):
            temp[i][j] = graph[n-1-j][i]
        
    for i in range(n):
        for j in range(n):
            graph[i][j] = temp[i][j]
            temp[i][j] = 0
    # print(graph)

# 아래로 숫자들을 떨어뜨립니다.
def drop():
    # next_grid를 0으로 초기화합니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = 0
    
    # 아래 방향으로 떨어뜨립니다.
    for j in range(n):
        # 같은 숫자끼리 단 한번만
        # 합치기 위해 떨어뜨리기 전에
        # 숫자 하나를 keep해줍니다.
        keep_num, next_row = NONE, n - 1
        
        for i in range(n - 1, -1, -1):
            if not graph[i][j]:
                continue
            
            # 아직 떨어진 숫자가 없다면, 갱신해줍니다.
            if keep_num == NONE:
                keep_num = graph[i][j];
            
            # 가장 최근에 관찰한 숫자가 현재 숫자와 일치한다면
            # 하나로 합쳐주고, keep 값을 비워줍니다.
            elif keep_num == graph[i][j]:
                temp[next_row][j] = keep_num * 2
                keep_num = NONE
                
                next_row -= 1
            
            # 가장 최근에 관찰한 숫자와 현재 숫자가 다르다면
            # 최근에 관찰한 숫자를 실제 떨어뜨려주고, keep 값을 갱신해줍니다.
            else:
                temp[next_row][j] = keep_num
                keep_num = graph[i][j]
                
                next_row -= 1
        
        # 전부 다 진행했는데도 keep 값이 남아있다면
        # 실제로 한번 떨어뜨려줍니다.
        if keep_num != NONE:
            temp[next_row][j] = keep_num
            next_row -= 1
    
    # next_graph를 graph에 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            graph[i][j] = temp[i][j]

# def remove_zero():
#     for j in range(n):
#         for i in range(n-1, 0, -1):
#             temp = graph[i][j]
#             if not temp:
#                 graph[i][j] = graph[i-1][j]
#                 graph[i-1][j] = 0
#     print(graph)

# 방향 회전
def rotate_dir(num):
    for _ in range(num):
        rotate()
    # 아래방향으로 떨어뜨림
    drop()
    for _ in range(4 - num):
        rotate()


dict_dir = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}

rotate_dir(dict_dir[direction])
for i in range(n):
    print(*graph[i])