n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0

a = set(a)
b = set(b)

for elem1 in a:
    if elem1 not in b:
        cnt += 1

for elem2 in b:
    if elem2 not in a:
        cnt += 1

print(cnt)