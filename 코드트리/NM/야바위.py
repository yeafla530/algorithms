n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

max_cnt = 0
for i in range(1, 4):
    cup = [0, 0, 0, 0]
    cup[i] = 1
    cnt = 0
    for a, b, c in arr:
        # 1, 2, 3
        temp = cup[a]
        cup[a] = cup[b]
        cup[b] = temp

        if cup[c] == 1:
            cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)