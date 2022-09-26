############### 1. Backtracking 
import sys
INT_MAX = sys.maxsize
# 각 동전을 사용하는 경우 / 사용하지 않는 경우로 나뉨 
# 모든 조합을 만들어 합이 m이 되는 경우에 대해서만 가능한 동ㅇ전의 개수 중 최소값
n, k = map(int, input().split())
coins = list(map(int, input().split()))
answer = []
result = INT_MAX


def find_result():
    global result
    # print(answer)
    value = 0
    for i in range(n):
        # print(answer)
        if answer[i]:
            value += coins[i]
    
    if value == k:
        result = min(result, sum(answer))


def choose(curr_num):
    if curr_num == n+1:
        find_result()
        return

    for i in range(2):
        answer.append(i)
        # print(curr_num)
        choose(curr_num+1)
        answer.pop()

choose(1)


if result == INT_MAX:
    print(-1)

else:
    print(result)