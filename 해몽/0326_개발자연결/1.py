# 각 블록마다 몇개랑 맞닿아 있는지 계산하기
import sys

si = sys.stdin.readline
n, m = map(int, input().split())

walls = [[0 for _ in range(m)] for _ in range(n)] # 2차원 담장을 의미
blocks = [[] for _ in range(n*m)] # blocks[i] := i 번 블록에 포함된 좌표들


cnt = 0 # 블록 번호
for i in range(n):
    # 행마다의 벽돌의 길이
    lengths = list(map(int, si().split())) # 3 1 1 2 => 1 1 1 2 3 4 4

    j = 0
    for x in lengths:
        cnt += 1
        for k in range(x):
            walls[i][j] = cnt
            blocks[cnt].append((i, j))
            j += 1


max_cnt = -1 # 핵심 블록이 맞닿아 있는 블록 개수
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for num in range(1, cnt+1): # num := 타켓 격자의 번호 결정
    mem = set() # 중복 제외 맞닿아 있는 블록 저장
    
    # 타켓 블록에 대해 몇개와 맞닿아있는지 확인
    for i, j in blocks[num]:
        # 인접한 4개의 칸에 어떤 블록이 존재하는지 확인
        for dx, dy in dirs:
            nx, ny = i + dx, j + dy # (nx, ny) := num번 블록과 인접한 좌표

            if not (0 <= nx < n and 0 <= ny < m): continue
            mem.add(walls[nx][ny])
    
    if num in mem: # 자기 자신 제외
        mem.remove(num) 
        
    if max_cnt < len(mem):
        max_cnt = len(mem)

print(max_cnt)


# for i in range(n*m):
    # print(*blocks[i])

# for i in range(n):
#     print(*walls[i])
'''
3 7
3 1 1 2
2 3 2
1 1 2 3

# walls
1 1 1 2 3 4 4
5 5 6 6 6 7 7
8 9 10 10 11 11 11

# blocks
(0, 0) (0, 1) (0, 2)
(0, 3)
(0, 4)
(0, 5) (0, 6)
(1, 0) (1, 1)
(1, 2) (1, 3) (1, 4)
(1, 5) (1, 6)
(2, 0)
(2, 1)
(2, 2) (2, 3)
(2, 4) (2, 5) (2, 6)


'''