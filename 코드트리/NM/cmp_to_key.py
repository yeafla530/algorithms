# 만약 국어 점수를 기준으로 정렬하되, 국어 점수가 30의 배수인 경우가 먼저 나오도록 하는 식

# 이렇게 lambda로 처리하기 애매한 경우에는 lambda 함수 대신 직접 기준을 정해주는 comparator 함수를 만들어줘야 합니다. 
#python3에서는 이 함수를 sort함수의 key 인자로 넘길때 
#꼭, functools내 cmp_to_key 함수를 import하여 cmp_to_key(compare) 식으로 감싸줘야 합니다.

# 정렬의 기준을 나타내는 함수인 compare 함수에는 인자를 2개 설정해줘야 합니다.
# 이를 x, y라 한다면 x가 앞에 있는 원소, y가 뒤에 있는 원소라 가정했을 때 
# 이 순서가 우리가 원하는 순서라면 0보다 작은 값을, 반대라면 0보다 큰 값을, 둘의 우선순위가 동일하다면 0을 반환하는 함수를 작성해줘야 합니다. 
# 이때 보통 반환값에 1, -1, 0을 사용합니다.
class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

from functools import cmp_to_key

students = [
    Student(90, 80, 90), # 첫 번째 학생
    Student(20, 80, 80), # 두 번째 학생
    Student(90, 30, 60), # 세 번째 학생
    Student(60, 10, 50), # 네 번째 학생
    Student(80, 20, 10), # 다섯 번째 학생 
]

# custom comparator를 직접 정의
# x가 앞에 있는 학생, y가 뒤에 있는 학생이라 가정했을 때
# 이 순서가 우리가 원하는 순서라면 0보다 작은 값을, 
# 반대라면 0보다 큰 값을
# 둘의 우선순위가 동일하다면 0을 반환하면 됩니다.
# 보통 반환값에 1, -1, 0을 사용합니다.

def compare(x, y):
    # x만 30의 배수라면 x가 더 앞에 있어야함
    if x.kor % 30 == 0 and y.kor % 30 != 0:
        return -1
    # y만 30의 배수라면 y가 더 앞에 있어야함
    if x.kor % 30 != 0 and y.kor % 30 != 0:
        return 1
    # 우선순위 동일
    return 0

# 점수의 총합 기준 오름차순
students.sort(key=cmp_to_key(compare))

for student in students: # 정렬 이후의 결과 출력
    print(student.kor, student.eng, student.math)



