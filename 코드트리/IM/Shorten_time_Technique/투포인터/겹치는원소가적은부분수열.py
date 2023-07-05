# hash + 투포인터

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# 같은 원소가 k개 이하로 들어있는
# 가장 긴 연속 부분 수열의 길이
j = 0
dict = {}
ans = 0
for i in range(1, n+1):
    while j + 1 <= n and dict.get(arr[j+1], 0) + 1 <= k:
        j += 1
        dict[arr[j]] = dict.get(arr[j], 0) + 1
        ans = max(ans, j - i + 1)

    dict[arr[i]] = dict.get(arr[i], 0) - 1
    if j + 1 <= n and i > j:
        j = i

    # print(i, j)
print(ans)