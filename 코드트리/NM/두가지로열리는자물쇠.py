n = int(input())

a, b, c = list(map(int, input().split()))
a1, b1, c1 = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if (abs(a-i) <= 2 or abs(a-i) >= n-2) and (abs(b-j) <= 2 or abs(b-j) >= n-2) and (abs(c-k) <= 2 or abs(c-k) >= n-2):
                cnt += 1
            elif (abs(a1-i) <= 2 or abs(a1-i) >= n-2) and (abs(b1-j) <= 2 or abs(b1-j) >= n-2) and (abs(c1-k) <= 2 or abs(c1-k) >= n-2):
                cnt += 1

print(cnt)