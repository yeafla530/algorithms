# 모이자 1문제 => 완전탐색 문제
# 모이자2는? LR테크닉 사용
# LR 테크닉 : 중복을 없애줌

# 마라톤 중간에 택시타기 문제
# LR 테크닉

# L : 1번부터 i번까지 인접한 숫자간의 쌍의 합이 전부 구해진것
# R: ~ 

# 잘 못풀면 DP로 푸는데 문제가 복잡해짐

# 집에있는 사람 수 : 3 2 4 3

#     3 2 4 3
# L   0 3 8

# 현재 2번집에 5명(3+2)명이 모여있음
# 그래서 3번집에 가는 사람은 
# 5명 (1, 2번집 )+ 3명 (첫번째 집에 있던 사람) = 8 
# == (3번집까지 가기위한 1, 2번 집의 이동거리)

# 다른분의 풀이
import sys
INT_MAX = sys.maxsize
n = int(input())
road = list(map(int, input().split()))

# 가중치를 맞추고
le = 0
ri = sum(road)

for i in range(n):
    le += road[i]
    ri -= road[i]
    # 중심점 찾기
    if le - ri > 0:
        limit = i
        break

ans = 0
for i in range(n):
    ans += (abs(i-limit)*road[i])

print(ans)
