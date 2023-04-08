n = 3 
visited = [False] * (n+1)
answer = []

def choose(cur_num):
    if cur_num == n+1:
        print(*answer)
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
            
        visited[i] = True
        answer.append(i)

        choose(cur_num+1)

        visited[i] = False
        answer.pop()


choose(1)