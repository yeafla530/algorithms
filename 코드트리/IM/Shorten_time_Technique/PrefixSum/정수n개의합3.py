n, k = map(int, input().split())
arr = [[0] * (n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

prefix = [[0]*(n+1) for _ in range(n+1)]

def get_sum(x1, x2, y1, y2):
    return prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i][j]
    
# print(prefix)

result = 0
for i in range(1, n-k+2):
    for j in range(1, n-k+2):
        # print(get_sum(i, i+k-1, j, j+k-1))
        result = max(result, get_sum(i, i+k-1, j, j+k-1))

print(result)

