n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(1, 10000):
    num = i * 2
    cnt = 0
    for a, b in arr:
        if a > num or num > b:
            break
        else:
            num *= 2
            cnt += 1
    if cnt == n:
        print(i)
        break
    