# itertools > combinations = 조합 
# nums = [1, 2, 3, 4]
# combi = list(combinations(nums, 개수))

# Counter > most_common(나타낼 개수) : 나타낼 개수만큼 가장 많이 나온 데이트 출력

# 정답 코드
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

