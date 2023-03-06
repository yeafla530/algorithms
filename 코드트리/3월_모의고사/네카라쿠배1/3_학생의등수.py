# 내 풀이
n = int(input())
arr = []
for i in range(n):
    math, eng = map(int, input().split())
    arr.append([math, eng, i])

arr.sort(key = lambda x: (-x[0], -x[1]))
ans = [0] * n
for i in range(n):
    ans[arr[i][2]] = i+1

for i in range(n):
    print(ans[i])


# 풀이
n = int(input())
stuent = []
sorted_list = [0] * n

for i in range(n):
    math, eng = map(int, input().split())
    student.append((i+1, math, eng))

student.sort(key = lambda x: (-x[1], -x[2]))

for i in range(n):
    idx = student[i][0]
    sorted_list[idx-1] = i+1

print(*sorted_list, sep="\n")