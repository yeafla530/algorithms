n = int(input())
studnets = []
for _ in range(n):
    s = list(input().split())
    studnets.append(s)

studnets.sort(key = lambda x: (x[1], -int(x[2])))


for name, h, w in studnets:
    print(name, h, w)