n = list(map(int, input()))
num = 0
for i in range(len(n)):
    num = num * 2 + n[i]

num *= 17
arr = []
while True:
    if num < 2:
        arr.append(num)
        break
    
    arr.append(num % 2)
    num = num // 2

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end="")

