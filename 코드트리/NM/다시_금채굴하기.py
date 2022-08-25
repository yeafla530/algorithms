# n * n
# m = gold가격 
n, m = map(int, input().split()) 
grid = [list(map(int, input().split())) for _ in range(n)]

max_gold = 0

# 채굴영역
def get_area(k):
    return k*k + (k+1)*(k+1)

# 주어진 k에 대하여 채굴 가능한 금의 개수를 반환합니다.
# row, col은 중심점
# k는 중심점과의 거리
def get_num_of_gold(row, col, k):
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 대각선안에 들어가는 금 추가
            if abs(row - i) + abs(col - j) <= k:
                cnt += grid[i][j]

    return cnt


# 규칙찾기 어려워요
# 격자의 각 위치가 마름모의 중앙일때 채굴 가능한 금의 개수 구하기
for row in range(n):
    for col in range(n):
        for k in range(2 * (n - 1) + 1):
            num_of_gold = get_num_of_gold(row, col, k)

            # 손해를 보지 않으면서 채굴할 수 있는 최대 금의 개수 저장 
            if num_of_gold * m >= get_area(k):
                max_gold = max(max_gold, num_of_gold)

print(max_gold)