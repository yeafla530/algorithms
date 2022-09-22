x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

sx = min(x1, a1)
ex = max(x2, a2)

se = min(y1, b1)
ee = max(y2, b2)

box = (ex - sx) * (ee - se)

print(box)

