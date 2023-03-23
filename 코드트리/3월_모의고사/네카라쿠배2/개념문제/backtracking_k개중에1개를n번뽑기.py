k, n = map(int, input().split())

def choose(cur_num):
    if cur_num == n+1:
        print(*arr)
        return
    
    for i in range(1, k+1):
        arr.append(i)
        choose(cur_num+1)
        arr.pop()

arr = []
choose(1)