# 구간 내 중복되는 숫자가 전혀 없는 경우 중 가능한 최대 구간

n = int(input())
arr = [0] + list(map(int, input().split()))
counting_arr = [0] * (10**5+1)

ans = 0
j = 0
for i in range(1, n+1):
    while j + 1 <= n and counting_arr[arr[j+1]] != 1:
        counting_arr[arr[j+1]] += 1
        j += 1
    

    ans = max(ans, j - i +1)

    counting_arr[arr[i]] -= 1

print(ans)
