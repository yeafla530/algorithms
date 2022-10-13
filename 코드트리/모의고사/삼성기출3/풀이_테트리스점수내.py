SHAPE_NUM = 19

# 변수 선언 및 입력:

# 가능한 모든 모양을 정의해줍니다.
blocks = [
    [[1, 1, 1, 1],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0]],

    [[1, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0]],

    [[0, 1, 0, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0]],

    [[1, 1, 1, 0],
     [1, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[1, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[1, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],

    [[1, 1, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0],
     [0, 0, 0, 0]],

    [[0, 0, 1, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[1, 0, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[1, 0, 0, 0],
     [1, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],

    [[0, 1, 1, 0],
     [1, 1, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[1, 1, 0, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[0, 1, 0, 0],
     [1, 1, 0, 0],
     [1, 0, 0, 0],
     [0, 0, 0, 0]],

    [[1, 0, 0, 0],
     [1, 1, 0, 0],
     [1, 0, 0, 0],
     [0, 0, 0, 0]],

    [[1, 1, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[0, 1, 0, 0],
     [1, 1, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 0]],

    [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]]

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
temp = [
    [0 for _ in range(m)]
    for _ in range(n)
]

ans = 0


def draw(shape, col, row):
    for dx in range(4):
        for dy in range(4):
            x, y = row + dx, col + dy
            if blocks[shape][dx][dy]:
                grid[x][y] = 1


def all_filled(row):
    for col in range(m):
        if not grid[row][col]:
            return False

    return True


def score(shape, col, row):
    # Step1. grid를 temp에 옮겨놓습니다.
    for i in range(n):
        for j in range(m):
            temp[i][j] = grid[i][j]

    # Step2. 움직이는 것을 종료하고 블럭의 최종 위치에 넣어줍니다.
    draw(shape, col, row)

    # Step3. 점수를 계산합니다.
    points = 0
    for row in range(n):
        if all_filled(row):
            points += 1

    # Step4. temp를 grid에 다시 옮겨줍니다.
    for i in range(n):
        for j in range(m):
            grid[i][j] = temp[i][j]

    return points


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


# 충돌은
# 격자를 벗어나게 되거나
# 해당 격자에 이미 블럭이 있을 경우에만 일어납니다.
def collision(x, y):
    return not in_range(x, y) or grid[x][y]


def can_go(shape, col, row):
    # 블록이 충돌이 일어나는 경우라면 진행할 수 없습니다.
    for dx in range(4):
        for dy in range(4):
            x, y = row + dx, col + dy
            if blocks[shape][dx][dy] and collision(x, y):
                return False

    return True


def can_place(shape, col):
    # 블럭을 이루고 있는 열 값이
    # 격자를 벗어나지는 않는지 확인합니다.
    for dx in range(4):
        for dy in range(4):
            if blocks[shape][dx][dy] and col + dy >= m:
                return False

    return True


def simulate(shape, col):
    # 떨어지는 블럭 중 가장 위에 있는 단위 블럭의 행 값입니다.
    for row in range(n):
        # 그 다음 행으로 내려갈 수 없다면
        # 점수를 계산합니다.
        if not can_go(shape, col, row + 1):
            return score(shape, col, row)

    return 0


# 모든 모양, 블럭을 떨어뜨릴 위치 (블럭의 가장 왼쪽 열의 위치)
# 를 정했을 때의 점수를 계산하여
# 그 중 최댓값을 갱신합니다.
for shape in range(SHAPE_NUM):
    for col in range(m):
        # 블럭을 해당 위치에 놓는 것이 가능한 경우에만 점수를 구합니다.
        if can_place(shape, col):
            ans = max(ans, simulate(shape, col))

print(ans)