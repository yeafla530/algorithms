k, n = map(int, input().split())
ans = []


def choose(cnt):
    if cnt == n:
        print(*ans)
        return

    for i in range(1, k+1):
        ans.append(i)
        choose(cnt+1)
        ans.pop()

choose(0)