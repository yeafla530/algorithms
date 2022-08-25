n = int(input())
arr = []
visited = [False] * (n+1)

def choose(cnt):
    if cnt == n+1:
        print(*arr)
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        arr.append(i)
        visited[i] = True
        
        choose(cnt+1)
        
        arr.pop()
        visited[i] = False


choose(1)