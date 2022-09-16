s = input()
d = {}

for x in s:
    d[x] = d.get(x, 0) + 1

is_none = True
for k, v in d.items():
    if v == 1:
        print(k)
        is_none = False
        break

if is_none:
    print(None)