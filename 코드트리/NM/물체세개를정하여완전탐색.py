n = 5
segments = [(1, 3), (2, 4), (5, 8), (6, 9), (7, 10)]

def get_max_overlappde_cnt(i1, i2, i3):
    count = [0] * 11
    for i in range(n):
        if i in [i1, i2, i3]:
            continue
        x1, x2 = segments[i]
        for j in range(x1, x2+1):
            count[j] += 1
    return max(count)

ans = 100
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            max_cnt = get_max_overlappde_cnt(i, j, k)
            ans = min(ans, max_cnt)

print(ans)