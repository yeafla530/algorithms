n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * (n)
# 처음과 끝은 1
min_val = 987654321
def find_min_cost(cnt, cur_idx, val):
    global min_val
    if cnt == n:
        if arr[cur_idx][0] == 0:
            return
        val += arr[cur_idx][0]
        min_val = min(val, min_val)
        return

    for i in range(1, n):
        if arr[cur_idx][i] == 0:
            continue
        if not visited[i]:
            visited[i] = True
            find_min_cost(cnt+1, i, val+arr[cur_idx][i])
            visited[i] = False


find_min_cost(1, 0, 0)
print(min_val)