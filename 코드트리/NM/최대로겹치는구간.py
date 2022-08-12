#  [x1, x2]에 대해 지점이 겹치는지가 궁금할 때에는 x1부터 x2까지, 구간이 겹치는지가 궁금할 때에는 x1부터 x2 - 1까지 표기를 진행
n = int(input())
dot = [0 for _ in range(201)]

for _ in range(n):
    a, b = map(int, input().split())
    a += 100
    b += 100

    for i in range(a, b):
        dot[i] += 1

print(max(dot))