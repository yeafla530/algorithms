s = input()
ans = ''
for i in range(len(s)):
    if s[i].isalpha():
        ans += s[i].lower()
    elif s[i].isdigit():
        ans += s[i]

print(ans)