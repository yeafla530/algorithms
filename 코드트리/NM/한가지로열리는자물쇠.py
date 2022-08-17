# 세자리숫자 중 세자리 모두다르고
# 세자리 합이 홀수인 수

# 한자리라도 주어지는 조합과 거리가 2이내면 열림
n = int(input())
key = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if abs(key[0]-i) <= 2 or abs(key[1]-j) <= 2 or abs(key[2]-k) <= 2:
                cnt += 1

print(cnt)