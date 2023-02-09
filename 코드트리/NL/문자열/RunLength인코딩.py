s = input()

w = s[0]
count = 1
ans = ''

for i in range(1, len(s)):
    if s[i-1] == s[i]:
        count += 1
    
    else:
        ans += w + str(count)
        count = 1
        w = s[i]

ans += w + str(count)

print(len(ans))
print(ans)
