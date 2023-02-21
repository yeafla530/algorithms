n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

dic = {}

ans = 0

for i in range(n):
    for j in range(n):
        sum_val = a[i] + b[j]
        if sum_val in dic:
            dic[sum_val] += 1
        
        else:
            dic[sum_val] = 1

for i in range(n):
    for j in range(n):
        diff = - c[i] - d[j]

        if diff in dic:
            ans += dic[diff]

print(ans)