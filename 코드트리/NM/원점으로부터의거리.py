n = int(input())

points = []
for i in range(n):
    a, b = map(int, input().split())
    points.append((a, b, i+1))

points.sort(key=lambda x: abs(x[0]) + abs(x[1]))

for point in points:
    _, _, i = point
    print(i)
