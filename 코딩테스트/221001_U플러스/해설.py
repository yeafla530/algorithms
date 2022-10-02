2.
pattern = input().strip()
new_pattern = ""
pairs = []
val, stk = 0, []
for c in pattern:
    if '0' <= c <= '9':
        val = val * 10 + (ord(c) - ord('0'))
    elif c == '(':
        stk.append(len(new_pattern))  # left parenthesis
        new_pattern += '('            # construct new pattern
        pairs.append([val, 0])        # save multiplication
        val = 0                       # reset value
    elif c == ')':
        new_pattern += ')'            # construct new pattern
        pair_idx = stk.pop(-1)        # memorize index of pair
        pairs[pair_idx][1] = len(new_pattern) - 1
        pairs.append(None)
    else:
        new_pattern += c
        pairs.append(None)
def construct(pattern, pairs, L, R):
    ret = ""
    i = L
    while i <= R:
        if pattern[i] == '(':
            # pairs[i] := (repeatition, index of paired parenthesis)
            ret += construct(pattern, pairs, i + 1, pairs[i][1] - 1) * pairs[i][0]
            i = pairs[i][1]
        else:
            ret += pattern[i]
        i += 1
    return ret
print(construct(new_pattern, pairs, 0, len(new_pattern) - 1))


3.
import sys
from typing import List, Tuple
si = sys.stdin.readline
n, m = map(int, si().split())
mappings = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
a = [[mappings[x] for x in si().strip()] for _ in range(n)]
ans = 100000000
dist = dict()
def toward(x: Tuple[int ,int]) -> Tuple[int, int]:
    d = a[x[0]][x[1]]
    return (x[0] + dirs[d][0], x[1] + dirs[d][1])
def is_facing(x: Tuple[int, int], y: Tuple[int, int]) -> bool:
    return toward(x) == y and toward(y) == x
def detect() -> Tuple[List[Tuple[int, int]], int]:
    facing, hash = [], 0
    for i in range(n):
        for j in range(m):
            # hash = (hash << 2) | a[i][j]
            hash = (hash * 4) + a[i][j]
            ni, nj = toward((i, j))
            if ni < 0 or nj < 0 or ni >= n or nj >= m:
                continue
            if is_facing((i, j), (ni, nj)):
                facing.append((i, j))
    return facing, hash
def backtracking(cnt: int) -> None:
    global ans
    candidates, hash = detect()
    if not candidates:                     # 아무도 서로를 마주하지 않음
        ans = min(ans, cnt)
    if dist.get(hash, 10000000) <= cnt:    # 더 빠르게 온 적이 있는 상황이면 return
        return
    dist[hash] = cnt
    if cnt + len(candidates) // 2 >= ans:  # ★ 남은 친구들이 한 번에 해결된다고 생각해도 정답이 개선되지 않는 경우
        return
    
    for i, j in candidates:
        for turn in range(4):
            a[i][j] = (a[i][j] + 1) % 4
            if turn != 3:
                v = 1 if turn != 2 else 2
                backtracking(cnt + v)
backtracking(0)
print(ans)


4.
import sys
si = sys.stdin.readline
N = int(si())
a = list(map(int, si().split()))
tree = [0 for _ in range(N * 2)]
B = N - 1
# fill the ternimal nodes
for i in range(B + 1, N * 2):
    tree[i] = a[i - B - 1]
# fill the internal nodes
special_cnt = 0
for i in range(B, 0, -1):
    tree[i] = max(tree[i * 2], tree[i * 2 + 1])
    if tree[i] == 1:
        special_cnt += 1
ans = special_cnt
for i in range(B + 1, N * 2):
    if tree[i] == 1: continue
    cur, changed_cnt = i // 2, 0
    # log(N)
    while cur:
        if tree[cur] == 0:
            changed_cnt += 1
        else:
            break
        
        cur //= 2
    ans = max(ans, special_cnt + changed_cnt)
print(ans)