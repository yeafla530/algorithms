n = int(input())
board = [[0] * (n+1)]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))
visited = [[0]*(n+1) for _ in range(n+1)]


# 예술성 점수 구하기
def count_score():
    # dfs사용해서 그룹 구하기
    # 닿는 면 개수 구하기
        # 사방을 구하면서 다른 숫자 (다른 그룹) count



# 4번 회전
for _ in range(4):
    # 1. 예술성 점수 구하기
    count_score()
    # 2. 회전하기
    rotate()