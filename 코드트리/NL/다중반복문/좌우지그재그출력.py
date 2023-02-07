n = int(input())

cnt = 1
for i in range(n):
    if i % 2 == 0:
        for _ in range(n):
            print(cnt, end=" ")
            cnt += 1
        cnt -= 1

    else:
        for _ in range(n):
            print(cnt, end=" ")
            cnt -= 1
        cnt += 1
    cnt += n
    print()