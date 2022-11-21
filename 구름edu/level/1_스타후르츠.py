n, t, c, p = map(int, input().split())
result = 0
seed = 1 + t

for i in range(1, n+1):
	if i == seed:
		result += c * p
		seed = i + t

		
print(result)