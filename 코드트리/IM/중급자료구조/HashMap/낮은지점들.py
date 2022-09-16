n = int(input())
d = {}
# 같은 x좌표는 y가 최대인 점만 남겨놓는다

for _ in range(n):
    x, y = map(int, input().split())

    if x not in d:
        d[x] = y
    
    else:
        d[x] = min(d[x], y)

# print(d)
result = 0
for k in d.keys():
    result += d[k]

print(result)
