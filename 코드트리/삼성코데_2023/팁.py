EMPTY = (-1, -1)
n = 4
marbles = [[EMPTY]*n for _ in range(n)]
marbles[1][1] = (0,4)

# 하나라도 True이면 True
ans = any([
    marbles[i][j] != EMPTY
    for i in range(n)
    for j in range(n)
])
print([
    marbles[i][j] != EMPTY
    for i in range(n)
    for j in range(n)
])
print(ans)


new = [(5, 1), (6, 3),  (3, 7), (7, 1), (5, 1), (6, 1), (4, 4)]
new.sort(key=lambda x: (x[0], x[1]))

print(new)

