arr = list(input())
n = len(arr)
cnt = 0

for i in range(n-2):
    for j in range(i+2, n-1):
        if arr[i] == "(" and arr[i+1] == "(" and arr[j] == ")" and arr[j+1] == ")":
            cnt += 1

# 나의 풀이
# for i in range(n-3):
#     for j in range(i+1, n-2):
#         for k in range(j+1, n-1):
#             for l in range(k+1, n):
#                 if arr[i] == "(" and arr[j] == "(" and arr[k] == ")" and arr[l] == ")" and j-i == 1 and l-k == 1:
#                     cnt += 1

print(cnt)