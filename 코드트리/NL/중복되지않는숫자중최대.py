# 중복하여 등정하지않는 최대값
n = int(input())
arr = list(map(int, input().split()))

max_num = -1

for num in arr:
    if max_num < num:
        count = 0

        for elem in arr:
            if elem == num:
                count+= 1
            
        if count == 1:
            max_num = num

print(max_num)


# 두번째 풀이
# 중복하여 등정하지않는 최대값
max_num = 1000

n = int(input())
arr = list(map(int, input().split()))

count = [0 for _ in range(max_num + 1)]

for elem in arr:
    count[elem] += 1


answer = -1
for n in range(max_num, -1, -1):
    if count[n] == 1:
        answer = n
        break

print(answer)