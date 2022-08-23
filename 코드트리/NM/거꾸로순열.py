n = int(input())
arr = []

def choose(cnt):
    if cnt == n:
        print(*arr)
        return
    
    for i in range(n, 0, -1):
        if i in arr:
            continue
        arr.append(i)
        choose(cnt+1)
        arr.pop()

choose(0)