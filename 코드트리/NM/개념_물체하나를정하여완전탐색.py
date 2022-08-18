n = 5
segments = [(1, 3), (2, 4), (5, 8), (6, 9), (7, 10)]

ans = 100
for i in range(n):
    # 한바퀴 끝나면 다시 0으로 초기화
    count = [0] * 11 # initalize
    for j in range(n):
        # 빼야하는 선분 제외
        if j == i:
            continue
        
        x1, x2 = segments[i]
        for k in range(x1, x2 + 1):
            count[k] += 1

    max_cnt = max(count)
    ans = min(ans, max_cnt)
print(ans)