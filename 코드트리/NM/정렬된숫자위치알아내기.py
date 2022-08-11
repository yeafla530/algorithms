n = int(input())
number = list(map(int, input().split()))

new = []
answer = [0 for _ in range(n)]
for i, j in enumerate(number):
    new.append((j, i))
# print(new)

new.sort(key=lambda x: (x[0], x[1]))
for i, (_, index) in enumerate(new, start=1):
    answer[index] = i
# print(new)

# print(answer)

for i in range(n):
    print(answer[i], end = ' ')