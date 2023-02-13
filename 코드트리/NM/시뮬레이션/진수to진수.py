a, b = map(int, input().split())
c = list(map(int, input()))

num = 0
# a진수 => 10 
for i in range(len(c)):
    num = num * a + c[i]

arr = []
# 10 => b진수로
while True:
    if num < b:
        arr.append(num)
        break
    
    arr.append(num %  b)
    num //= b

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end="")    
