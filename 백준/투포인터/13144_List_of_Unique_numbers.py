# 수열에서 연속한 1개 이상의 수를 뽑았을 때
# 같은 수가 여러번 등장하지 않는 경우의 수 구하기

n = int(input())
arr = list(map(int, input().split()))

counting_arr = [0] * (10**5 + 1)
result = 0
start, end = 0, 0

while start != n and end != n:
    if not counting_arr[arr[end]]: # start부터 end까지 중복 숫자 없으면
        counting_arr[arr[end]] = True
        end += 1
        result += end - start # end포함해 만들 수 있는 수열 개수
    else: # end를 포함하여 만들 수 있는 수열의 개수
        while counting_arr[arr[end]]:
            counting_arr[arr[start]] = False
            start += 1

    print(start, end)


print(result)
