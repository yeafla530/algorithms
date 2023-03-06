# 동전의 합을 노드, 동전 하나 사용하는 것을 간선으로 생각
# 가중치가 전부 1인 그래프 > 정점 0 ~ m까지 최단거리 구하는 문제가 됨
# r은 주어지는 동전 가중치중 가능한 최대값
# 합이 m보다 커지면, 최종적으로 m을 만들기 위해 최소 1개 이상의 음수 가중치인 동전 사용
# 계산과정에서 m+r을 넘기지 않으면 합 m을 만드는것이 항상가능

from collections import deque
import sys

INT_MAX = sys.maxsize
MAX_NUM = 20000
n, m = map(int, input().split())
coins = list(map(int, input().split()))

q = deque()
visited = [False] * (MAX_NUM+1)
step = [0] * (MAX_NUM + 1)

ans = INT_MAX

# 1에서 20000사이 안에서만 합을 만들어도 항상 최단거리 구할 수있으므로
# 그 범위 안에 들어오는지 확인
def in_range(n):
    return 0 <= n <= MAX_NUM


def can_go(n):
    return in_range(n) and not visited[n]

# queue에 새로운 위치 추가하고 방문여부 표시
# 시작점으로부터 최단거리 값 갱신
def push(num, new_step):
    q.append(num)
    visited[num] = True
    step[num] = new_step

# visited이유
# 가장 먼저 방문하게 되면 최솟값
def find_min():
    global ans
    while q:
        curr_num = q.popleft()
        for coin in coins:
            new_num = curr_num + coin
            if can_go(new_num):
                push(new_num, step[curr_num]+1)

    if visited[m]:
        ans = step[m]



push(0, 0)
find_min()

if ans == INT_MAX:
    ans = -1

print(ans)