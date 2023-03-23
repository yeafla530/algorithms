# Ad-hoc
n = int(input())
arr = list(map(int, input().split()))
arr.sort()


sum_val = 0
for elem in arr:
    if sum_val + 1 < elem:
        break
    sum_val += elem

print(sum_val+1)


# 시간초과 답
n = int(input())
arr = list(map(int, input().split()))
possible_sums = set()

def combination(idx, sum_val):
    if idx == n:
        possible_sums.add(sum_val)
        return
    
    # idx번지수 선택하지 않는 경우
    combination(idx + 1, sum_val)
    combination(idx+1, sum_val+arr[idx])


combination(0, 0) # 

num = 1
while True:
    if num not in possible_sums:
        print(num)
        break
    
    num += 1
