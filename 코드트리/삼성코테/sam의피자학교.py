# 4 3
# 26 9 29 14

n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_v = min(arr)
max_v = max(arr)
cnt = 0


# 1. 밀가루 추가
def add_flour():
    # 밀가루 양이 적은 곳에 밀가루 1추가
    for i in range(n):
        if arr[i] == min_v:
            arr[i] += 1


# 2. 도우 말기
def roll_dough():

    for i in range(n):
        board[0][i] = arr[i]

    pivot = 0
    w = 1
    h = 1
    # cnt = 10
    # 높이만큼 말아주기
    while pivot + w + h <= n:
    # while cnt > 0:
    #     cnt -= 1
        temp = [[0]*w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                # print(i, pivot+j)
                temp[i][j] = board[i][pivot+j]
                board[i][pivot+j] = 0


        # 반시계방향 회전
        temp = list(map(list, zip(*temp)))[::-1]


        # print(board)

        pivot += w

        for i in range(w):
            for j in range(h):
                # print(i + 1, pivot + j)
                board[i + 1][pivot + j ] = temp[i][j]
        # print(board)
        if h == w:
            h += 1
        elif h > w:
            w += 1

        # print(pivot, w, h)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 3. 도우 눌러주기
def push_dough():
    next_board = [[0]*n for _ in range(n)]
    dxs = [1, 0]
    dys = [0, 1]

    for i in range(n):
        for j in range(n):
            next_board[i][j] = board[i][j]

    # print(next_board)
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for dx, dy in zip(dxs, dys):
                    nx = i + dx
                    ny = j + dy
                    if in_range(nx, ny) and board[nx][ny]:
                        a = board[i][j]
                        b = board[nx][ny]

                        d = abs(a - b) // 5
                        # print(a, b, d)
                        if a >= b:
                            next_board[i][j] -= d
                            next_board[nx][ny] += d
                        else:
                            next_board[i][j] += d
                            next_board[nx][ny] -= d

    for i in range(n):
        for j in range(n):
            board[i][j] = next_board[i][j]


    # 다시 펴기
    idx = 0
    for j in range(n):
        for i in range(n):
            if board[i][j]:
                # print(i, j)
                arr[idx] = board[i][j]
                idx += 1

    # print(arr)




# 동시에 진행
# 상하좌우로 인접한 밀가루 |a-b|를 5로 나눈 몫d
# 작은값에 + d, 큰값에 -d

# 눌러주기 => 2차원 배열이라 생각했을 때
# 열이 작은값부터, 열이 같으면 행이 작은값부터

# 4. 도우 접기
def fold_dough():
    for i in range(n):
        board[0][i] = arr[i]

    m = len(arr) // 2
    p = 0
    w = m
    h = 1
    for _ in range(2):
        temp = [[0] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                # print("+++++++++++++++")
                # print(i, p+j)

                temp[i][j] = board[i][p+j]
                board[i][p + j] = 0
        # print("+++++++++++++++")
        #
        # print(temp)

        # 반시계방향 회전
        for _ in range(2):
            temp = list(map(list, zip(*temp)))[::-1]
        p += m
        # print("p, w, h", p, w, h)
        for i in range(h):
            for j in range(w):
                board[h+i][p + j] = temp[i][j]
        m //= 2
        w = m
        h *= 2
        # print(board)

# 반으로 접고
# 한번더 반으로 접기

while max_v - min_v > k:
    cnt += 1
    # 1. 밀가루 추가
    add_flour()
    # 2. 도우 말기
    board = [[0] * (n) for _ in range(n)]
    roll_dough()
    # 3. 도우 눌러주기
    push_dough()
    board = [[0] * n for _ in range(n)]
    # # 4. 두번 접기
    fold_dough()
    # # 5. 도우 눌러주기
    push_dough()
    # print(arr)

    min_v = min(arr)
    max_v = max(arr)

print(cnt)
