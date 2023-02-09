n = int(input())

num = 0
for i in range(n):
    num += int(input())

num = str(num)

num = num[1:] + num[0]
print(num)