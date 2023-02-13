binary = list(map(int, input()))
ans = 0

for i in range(len(binary)):
    ans = ans * 2 + binary[i]

print(ans)
