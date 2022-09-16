n = int(input())
d = {}

max_result = 0
for _ in range(n):
    key = input()
    d[key] = d.get(key, 0) + 1

    max_result = max(max_result, d[key])

print(max_result)