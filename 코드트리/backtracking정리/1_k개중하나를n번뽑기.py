k, n = map(int, input().split())
answer = []

def choose(cnt):
    if cnt == n:
        print(*answer)
        return
    
    for i in range(1, k+1):
        if len(answer) >= 2 and answer[-1] == i and answer[-2] == i:
            continue
        answer.append(i)
        choose(cnt+1)
        answer.pop()

choose(0)