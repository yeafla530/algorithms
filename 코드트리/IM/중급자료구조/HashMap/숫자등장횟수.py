n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = {}
for x in a:
    d[x] = d.get(x, 0) + 1

# print(d)
for y in b:
    if y not in d:
        print(0, end=" ")
    else:
        print(d[y], end=" ")

