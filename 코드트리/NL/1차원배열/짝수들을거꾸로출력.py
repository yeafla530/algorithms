n = int(input())
arr = map(int, input().split())

new = list()
for elem in arr:
    if elem % 2 == 0:
        new.append(elem)

for i in range(len(new)-1, -1, -1):
    print(f"{new[i]}", end=" ")


# 정답 풀이
n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    if arr[i] % 2 == 0:
        print(arr[i], end=" ")