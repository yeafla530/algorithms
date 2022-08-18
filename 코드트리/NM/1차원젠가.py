# 내 풀이
n = int(input())
zenga = [int(input()) for _ in range(n)]

for _ in range(2):
    a, b = map(int, input().split())
    zenga = zenga[:a-1] + zenga[b:]
    # print(zenga)

# print(zenga)
if len(zenga) == 0:
    print(0)
else:
    print(len(zen))
    for i in range(len(zenga)):
        print(zenga[i])


# 시뮬레이션 방식
n = int(input())
numbers = [int(input()) for _ in range(n)]
end_of_array = n

def cut_array(start, end):
    global end_of_array
    temp = []
    # 구간 외의 부분만 temp 배열에 순서대로 저장
    for i in range(end_of_array):
        # start보단 작고, end보단 큰것들만 넣어줌
        # if i < start or i > end:
        if not start <= i <= end:
            temp.append(numbers[i])
        
    # temp 배열을 다시 numbers 배열로 옮겨줌
    end_of_array = len(temp)
    for i in range(end_of_array):
        numbers[i] = temp[i]

    return numbers


for i in range(2):
    s, e = map(int, input().split())
    # [s, e]
    # 젠가 자르기
    numbers = cut_array(s-1, e-1)

print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])