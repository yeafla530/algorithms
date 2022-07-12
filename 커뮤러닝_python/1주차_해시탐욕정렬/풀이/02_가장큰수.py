def solution(numbers):
    answer = ''
    numbers = [str(x) for x in numbers]
    # 11번 통과 못함
    # 0만 여러개 주어진다면! => 0으로 return

    # 해당수를 4번반복해서 4자리수까지 slice
    numbers.sort(key=lambda x : (x*4)[:4], reverse=True)
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    return answer