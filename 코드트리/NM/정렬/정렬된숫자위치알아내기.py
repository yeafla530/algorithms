n = int(input())
arr = list(map(int, input().split()))
new_arr = []

for i in range(n):
    new_arr.append((i+1, arr[i]))

new_arr.sort(key=lambda x: x[1])

pos = [0] * n

for i in range(n):
    # print(new_arr[i][0])
    pos[new_arr[i][0]-1] = i+1

print(*pos)

# 답지
n = int(input())
arr = list(map(int, input().split()))

numbers = [(num, i) for i, num in enumerate(arr)]
answer = [0 for _ in range(n)]

numbers.sort(key=lambda x: (x[0], x[1]))
print(numbers)

for i, (_, index) in enumerate(numbers):
    answer[index] = i+1

print(*answer)