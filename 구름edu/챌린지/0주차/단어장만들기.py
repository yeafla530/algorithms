
n, m = map(int, input().split())
arr = []

for _ in range(n):
	word = input()
	arr.append(word)

arr.sort(key=lambda x: (len(x), x))

print(arr[m-1])