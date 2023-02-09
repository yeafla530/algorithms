# 내풀이
s = input()
ans = ""

for i in range(1, len(s), 2):
    ans += s[i]

print(ans[::-1])


string = input()

idx = len(string)
if idx % 2 == 0:
    idx -= 1

for i in range(idx, -1, -2):
    print(string[i], end="")