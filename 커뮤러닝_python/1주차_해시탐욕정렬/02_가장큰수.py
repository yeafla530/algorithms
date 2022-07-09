# 처음에 조합으로 풀려했지만 실패
def solution(numbers):
    numbers = list(map(str, numbers))
    # 블로그 참고
    # 하지만 3이 30보다 앞에 와야한다. number는 1000이하의 숫자이므로 최대값을 생각해 3을 곱해줬고,
    # 3을 곱하게 되면 [999, 555, 343434, 303030, 333] 이렇게 될 것이고, 정렬을 하게 되면 [999, 555, 343434, 333, 303030]이 된다.
    numbers.sort(key=lambda x: x * 3, reverse = True)

    return str(int(''.join(numbers)))