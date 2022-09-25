# L 배열 = 1번부터 i번까지 인접한 숫자간의 쌍의 합이 전부 구해짐
# R 배열 = i번부터 N번까지 인접한 숫자간의 쌍의 합이 전구 구해짐
arr = [0, 3, 6, 2, 6, 7, 5, 2]
L = [0] * 8
R = [0] * 8
n = 7

# L배열 채우기
L[1] = 0
for i in range(2, n+1):
    L[i] = abs(arr[i] - arr[i-1]) + L[i-1]

# R배열 채우기
R[n] = 0
for i in range(n-1, 0, -1):
    R[i] = abs(arr[i] - arr[i+1]) + R[i+1]

# 5번째를 제외했을 때 답
print(L[4] + R[6] + abs(arr[6] - arr[4]))
