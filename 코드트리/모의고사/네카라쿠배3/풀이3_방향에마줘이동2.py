# 시뮬레이션 문제




## 다른분의 풀이
# 전체 적인 x, y 합차 구해주고
# 그 후에 뺄 것의 반대 방향의 거리만큼 이동한 x, y구해준다 
import sys
INT_MAX = sys.maxsize
N = int(input())
x, y = [], []
for _ in range(N):
    w, l = map(str, input().split())
    l = int(l)

    if w == 'E':
        x.append(l)
    elif w == 'W':
        x.append(-l)
    elif w == 'N':
        y.append(l)
    elif w == 'S':
        y.append(-l)
        
ans = INT_MAX
x_sum, y_sum = sum(x), sum(y)
for i in range(len(x)):
    ans = min(ans, abs(y_sum) + abs(x_sum - x[i]))

for i in range(len(y)):
    ans = min(ans, abs(x_sum) + abs(y_sum - y[i]))

print(ans)