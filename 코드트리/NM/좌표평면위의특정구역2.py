import sys
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize
for i in range(n):
    x1, x2 = sys.maxsize, 1
    y1, y2 = sys.maxsize, 1
    for j, (x, y) in enumerate(arr):
        if i == j:
            continue
        # print(x, y, arr[j][0], arr[j][1])
        x1 = min(x1, x)
        y1 = min(y1, y)

        x2 = max(x2, x)
        y2 = max(y2,y)

        # print(y1, x1, y2, x2, arr[i][0], arr[i][1])
    

    ans = min(ans, abs(x2-x1)*abs(y2-y1))

print(ans)

