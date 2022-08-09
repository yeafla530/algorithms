# 10개 정수입력받아 500미만의 수 중 가장 큰수와 500초과 수중 가장 작은 수
arr = list(map(int, input().split()))
max1 = -1
max2 = 1001

for i in arr:
    if i > max1 and i < 500:
        max1 = i
    
    elif i < max2 and i > 500:
        max2 = i

print(max1, max2)