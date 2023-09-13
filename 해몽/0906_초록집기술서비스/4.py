# 문제 4. 가장 긴 짝수 연속한 부분 수열 백준 22862
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ans = 0
j = 0
cnt = 0

# 구간에서 홀수의 개수가 k개 이하이고, 최대 부분수열 길이를 찾기
for i in range(1, n+1):
    while j + 1 <= n and cnt < k:
        if arr[j+1] % 2 == 1:
            cnt += 1
        j += 1
            

    while j + 1 <= n and arr[j+1] % 2 == 0:
        j += 1
        
    
    ans = max(ans, (j - i + 1)-cnt)
    if arr[i] % 2 == 1:
        cnt -= 1

print(ans)



# # 투포인터 기본 개념
# n, s = map(int, input().split())
# arr = [0] + list(map(int, input().split()))

# ans = 987654321
# j = 0
# sum_val = 0

# for i in range(1, n+1):
#     while j + 1 <= n and sum_val < s:
#         j += 1
#         sum_val += arr[j]
    
#     if sum_val < s:
#         break

#     ans = min(ans, j - i + 1)
#     sum_val -= arr[i]

# if ans == 987654321:
#     print(-1)

# else:
#     print(ans)

# # 투포인터 개념 2
# n = int(input())
# arr = [0] + list(map(int, input().split()))
# count_arr = [0] * 100001

# ans = 0
# j = 0

# for i in range(1, n+1):
#     while j + 1 <= n and count_arr[arr[j+1]] != 1:
#         j += 1
#         count_arr[arr[j]] += 1

#     ans = max(ans, j - i + 1)
#     count_arr[arr[i]] -= 1

# print(ans)


# # 투포인터 개념3
# n, m = map(int, input().split())
# a = [0] + list(map(int, input().split()))
# b = [0] + list(map(int, input().split()))

# def is_sub():
#     i = 0
    
#     for j in range(1, m+1):
#         while i <= n and a[i] != b[j]:
#             i += 1
        
#         if i == n+1:
#             return False 
        
#         else:
#             i += 1
        
#     return True


# if is_sub():
#     print("Yes")
# else:
#     print("No")
