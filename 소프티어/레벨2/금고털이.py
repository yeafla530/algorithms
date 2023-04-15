w, n = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
jewels.sort(key=lambda x : -x[1])

total_v = 0
for x in range(n):
    m, p = jewels[x]
    # 남은 무게가 현재 광물 무게보다 클 때

    if w > m:
        total_v += m * p
        w -= m
    # 작을 때
    else:
        total_v += w * p
        break
print(total_v)