# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
checked = [
    [False] * n
    for _ in range(n)
]
ans = 0


# 현재까지 고른 쌍의 수가 cnt이고
# 지금까지 고른 쌍으로부터 얻은
# 수들의 총 합을 sum_val이라고 했을 때
# 계속해서 탐색을 진행합니다.
def find_max(cnt, sum_val):
    global ans

    # 최대 k개의 쌍을 겹치지 않게 골라 
    # 얻을 수 있는 아름다움의 총 합 중
    # 최댓값을 갱신해줍니다.
    ans = max(ans, sum_val)

    # 이미 k개의 쌍을 골랐다면
    # 퇴각합니다.
    if cnt == k:
        return

    # 새로운 쌍을
    # (i, j) 위치를 기점으로 찾아봅니다.
    for i in range(n):
        for j in range(n):
            # Case 1. 
            # (i, j)와 (i, j + 1) 이렇게 2개로 새로운 쌍을 만들어 봅니다.
            # 아직 두 위치 모두 선택된 적이 없어야만 가능합니다.
            if j + 1 < n and not checked[i][j] and not checked[i][j + 1]:
                checked[i][j] = checked[i][j + 1] = True
                find_max(cnt + 1, sum_val + arr[i][j] + arr[i][j + 1])
                checked[i][j] = checked[i][j + 1] = False

            # Case 2.
            # (i, j)와 (i + 1, j) 이렇게 2개로 새로운 쌍을 만들어 봅니다.
            # 아직 두 위치 모두 선택된 적이 없어야만 가능합니다.
            if i + 1 < n and not checked[i][j] and not checked[i + 1][j]:
                checked[i][j] = checked[i + 1][j] = True
                find_max(cnt + 1, sum_val + arr[i][j] + arr[i + 1][j])
                checked[i][j] = checked[i + 1][j] = False


# 최댓값을 찾아줍니다.
find_max(0, 0)
print(ans)