# 사용했어야 하는 중복수열 코드
# 나는 함수로 중복수열 함수 사용했음
n = 3
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

def choose(curr_num):
    if curr_num == n+1:
        print_answer()
        return

    for i in range(10, 50, 10):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()
    


choose(1)