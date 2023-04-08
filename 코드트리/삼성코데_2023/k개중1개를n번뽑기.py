n = 3
answer = []



def choose(cnt):
    if cnt == n:
        print(*arr)
        return

    for i in range(2):
        answer.append(i)
        choose(cnt+1)
        answer.pop()


choose(0)