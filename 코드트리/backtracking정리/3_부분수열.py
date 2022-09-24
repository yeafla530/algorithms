import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력 :
n, m = tuple(map(int, input().split()))
coins = list(map(int, input().split()))

ans = INT_MAX


def find_min(idx, sum_val, cnt):
    global ans

    # 종료조건이 되면
    # 퇴각합니다.
    if idx == n:
        # 합이 정확히 m인 경우에 
        # 답을 갱신합니다.
        if sum_val == m:
            ans = min(ans, cnt)
        return

    # idx번지 수를 선택하지 않는 경우입니다.
    find_min(idx + 1, sum_val, cnt)
    # idx번지 수를 선택하는 경우입니다.
    find_min(idx + 1, sum_val + coins[idx], cnt + 1)

   
# 최소 동전의 수를 찾아봅니다.
find_min(0, 0, 0)

# 불가능하다면
# 답은 -1이 됩니다.
if ans == INT_MAX:
    ans = -1

print(ans)