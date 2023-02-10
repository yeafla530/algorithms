n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

res = 0

for i in range(n-3+1):
    for j in range(n-3+1):
        s = 0
        for a in range(3):
            for b in range(3):
                if grid[i+a][j+b] == 1:
                    s += 1
        
        if s > res:
            res = s

print(res)