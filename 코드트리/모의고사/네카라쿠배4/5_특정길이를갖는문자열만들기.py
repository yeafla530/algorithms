n, m = map(int, input().split())
string = list(input().split())
visited = [0] * n
answer = ""
# g = []

def dp(cnt, s):
    global answer
    if cnt > m:
        return
    if cnt == m:
        if answer == "" or answer > s:
            answer = s
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dp(cnt+len(string[i]), s+string[i])
            visited[i] = 0


dp(0, '')
# print(g)
# g.sort()

if answer != "":
    # print(g[0])
    print(answer)
else:
    print(-1)