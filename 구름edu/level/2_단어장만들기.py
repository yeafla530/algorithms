
n, k = map(int, input().split())
arr = [input() for _ in range(n)]

arr.sort(key=lambda x: (len(x), x))

print(arr[k-1])