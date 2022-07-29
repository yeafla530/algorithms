n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

d = [0] * 100
d[0] = array[0]
d[1] = array[1]

for i in range(2, n+1):
    d[i] = max(d[i-2]+array[i], d[i-1])

print(d[n-1])