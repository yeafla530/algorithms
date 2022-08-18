n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def get_max_coin(i, j):
    c = 0
    for x in range(i, i+3):
        for y in range(j, j+3):
            if arr[x][y] == 1:
                c += 1

    return c   

max_coin = 0
for i in range(n-3+1):
    for j in range(n-3+1):
        coin = get_max_coin(i, j)
        max_coin = max(max_coin, coin)


print(max_coin)