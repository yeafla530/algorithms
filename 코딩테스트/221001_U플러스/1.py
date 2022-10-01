def solution(arr):
    answer = 0
    # 애너그램 관계를 찾아라
    d = {}
    new_number = 0

    for x in arr:
        new_number = ''.join(sorted(str(x)))
        print(new_number)
        d[new_number] = d.get(int(new_number),0) + 1

    return len(d)


solution([122, 1814, 121, 1481, 1184])