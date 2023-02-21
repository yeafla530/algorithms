n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = {}
for elem in arr:
    if elem in d:
        d[elem] += 1
    
    else:
        d[elem] = 1
a = []
for key in d:
    a.append((key, d[key]))


a.sort(key=lambda x: (-x[1], -x[0]))

# print(a)
for i in range(k):
    print(a[i][0], end=" ")