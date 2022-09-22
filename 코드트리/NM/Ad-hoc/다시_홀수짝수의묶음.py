# 최대 묶음의 개수 = 짧게 잘라라
n = int(input())
arr = list(map(int, input().split()))

even = 0
odd = 0

for a in arr:
    if (a % 2 == 0):
        even += 1
    else:
        odd += 1

group_num = 0
while True:
    # 묶음이 짝수개일때
    if group_num % 2 == 0:
        # 짝수가 있다면 -1
        if even:
            even -= 1
            group_num += 1
        # 홀수가 있다면
        elif odd >= 2:
            odd -= 2
            group_num += 1
        # 홀수가 1개고 짝수인 수가 없다면
        # 그 전 그룹과 합쳐주기
        else:
            if odd > 0:
                group_num -= 1
            
            break
            
    else:
        # 홀수일때
        if odd:
            odd -= 1
            group_num += 1
        
        # 홀수가 없을 때
        else:
            break

print(group_num)