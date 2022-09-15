# NM의 객체정렬을 풀어봐야함
# 오 나는 기초가 잡혔나봄 
# 객체가 만들어서 정렬을 해야한다가 기본


###### class풀이
# 클래스 선언
class Student:
    def __init__(self, math, eng, number):
        self.math = math
        self.eng = eng
        self.number = number


# 변수 선언 및 입력:
n = int(input())

# 어느 학생이 어떤 등수를 받았는지에 대한
# 정보를 저장합니다.
num_to_rank = [0] * n

students = []
for i in range(n):
    math, eng = tuple(map(int, input().split()))
    # Student 객체를 생성해 리스트에 추가합니다.
    students.append(Student(math, eng, i))

# custom comparator를 활용한 정렬
# 수학 점수, 영어 점수 순으로 내림차순 정렬합니다. 
students.sort(key=lambda x: (-x.math, -x.eng))

"""
30 10 3 <- 1등
20 90 4 <- 2등
20 80 2 <- 3등
10 50 1 <- 4등
"""

# for i in range(1, n + 1):
#     num_to_rank[students[i].number] = i
#                # 0 1 2 3 4
# num_to_rank = [    4 3 1 2]


# 어느 학생이 어떤 등수를 받았는지를 표시해줍니다.
for i in range(n):
    num_to_rank[students[i].number] = i + 1
 
# 각 학생의 등수를 출력합니다.
for i in range(n):
    print(num_to_rank[i])


###### rank도 같이 담아주는 형식
# 클래스 선언
class Student:
    def __init__(self, math, eng, number, rank=-1):
        self.math = math
        self.eng = eng
        self.number = number
        self.rank = rank


# 변수 선언 및 입력:
n = int(input())

students = []
for i in range(n):
    math, eng = tuple(map(int, input().split()))
    # Student 객체를 생성해 리스트에 추가합니다.
    students.append(Student(math, eng, i))

# custom comparator를 활용한 정렬
# 수학 점수, 영어 점수 순으로 내림차순 정렬합니다. 
students.sort(key=lambda x: (-x.math, -x.eng))

for i in range(n):
    students[i].rank = i + 1

# 학생 번호순으로 다시 정렬
students.sort(key=lambda x: x.number)

# 등수 출력
for i in range(n):
    print(students[i].rank)


"""
10 50 1 4등
20 80 2 3등
30 10 3 1등
20 90 4 2등
"""



###### tuple풀이
## class를 만드는거 귀찮으니 tuple사용하는게 편리
