import sys
INT_MAX = sys.maxsize

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
x = 0
y = 0

mapper = {
    "E": 0,
    "W": 1,
    "S": 2,
    "N": 3
}

dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

for a in arr:
    s, m = a
    i = mapper[s]

    x += dxs[i] * int(m)
    y += dys[i] * int(m)


result = INT_MAX
for a in arr:
    nx = x
    ny = y
    s, m = a
    i = mapper[s]

    nx -= dxs[i] * int(m)
    ny -= dys[i] * int(m)

    result = min(result, abs(nx) + abs(ny))
    

print(result)



