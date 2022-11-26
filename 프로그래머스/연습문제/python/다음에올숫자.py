def solution(common):
    answer = 0
    num1 = common[1] - common[0]
    if common[0] != 0:
        num2 = common[1] / common[0]
    else:
        num2 = 0
    result_num = 0
    kind = '등비'

    for i in range(2, len(common)):
        if num1 == (common[i] - common[i-1]):
            result_num = num1
            kind = '등차'
        elif num2 == (common[i] / common[i-1]):
            result_num = num2
            kind = '등비'

    if kind == '등비':
        answer = common[-1] * result_num
    else:
        answer = common[-1] + result_num

    return answer


def solution(common):
    a, b, c = common[:3]
    if (b-a) == (c-b):
        return common[-1] + (b-a)
    else:
        return common[-1] * (b//a)

    