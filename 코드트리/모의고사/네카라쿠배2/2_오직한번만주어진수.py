# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))
freq = {}

# 각 수가 몇 번씩 나왔는지 기록합니다.
for elem in arr:
    freq[elem] = freq.get(elem, 0) + 1

# 정확히 1번만 나온 수 중
# 등장한 최초 위치를 구해줍니다.
ans = -1
for i in range(n - 1, -1, -1):
    # 최초로 나왔다면 답을 갱신합니다. 
    if freq[arr[i]] == 1:
        ans = arr[i]

print(ans)