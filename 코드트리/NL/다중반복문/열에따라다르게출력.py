n = int(input())

cnt = 1
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            print(cnt, end=" ")
            if j < n-1:
                cnt += 1
            else:
                cnt += 2     
    else:
        for j in range(n):
            print(cnt, end=" ")
            if j < n-1:
                cnt += 2
            else:
                cnt += 1

    print()