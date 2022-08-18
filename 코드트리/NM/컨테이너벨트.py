n, t = map(int, input().split())
# 첫번째는 순서 그대로 두번째는 reverse
# 1차원 배열로 생각해서 오른쪽으로 민것으로 생각
# 1 2 3 6 5 1
u = list(map(int, input().split()))
d = list(map(int, input().split()))
a = u + d

# 3. moduler
cnt = t % (2*n)
a = a[-cnt:] + a[:-cnt] 

# 2. 슬라이싱
# for i in range(t % (2*n)):
    #a = a[-1:] + a[:-1]

# 1. 시뮬레이션 
# t초오른쪽으로 한칸씩 밀기
# for i in range(t):
    # temp = a[-1]
    # 맨오른쪽-1 idx부터 0 idx가는 방향으로 움직임
    # 그래야 덮어씌워지지않음
    # for j in range(2*n-2, -1, -1):
    #     a[j+1] = a[j]
    # a[0] = temp

# 출력법2
print(*a[:n])
print(*a[n:])

# 출력법1
# for i in range(n):
#     print(a[i], end=" ")
# print()

# for i in range(n):
#     print(a[i+n], end=" ")

