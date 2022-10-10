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
    board = [[0] * n for _ in range(n // 2)]
    pivot = 0
    w = 1
    h = 1
    # 높이만큼 말아주기
    while pivot + w + h < n:
        pivot += w
        if h == w:
            h += 1
        elif h > w:
            w += 1
        print(pivot, w, h)


# 높이보다 바닥 len이 작으면 stop

# 3. 도우 눌러주기
def push_dough():


# 동시에 진행
# 상하좌우로 인접한 밀가루 |a-b|를 5로 나눈 몫d
# 작은값에 + d, 큰값에 -d

# 눌러주기 => 2차원 배열이라 생각했을 때
# 열이 작은값부터, 열이 같으면 행이 작은값부터

# 4. 도우 접기
def fold_dough():


# 반으로 접고
# 한번더 반으로 접기

while max_v - min_v > k:
    cnt += 1
    # 1. 밀가루 추가
    add_flour()
    # 2. 도우 말기
    roll_dough()
    # 3. 도우 눌러주기
    push_dough()
    # 4. 두번 접기
    fold_dough()
    # 5. 도우 눌러주기
    push_dough()