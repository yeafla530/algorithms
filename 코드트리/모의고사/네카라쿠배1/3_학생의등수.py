# 등수매기기
# 1. 수학 점수가 높은 학생의 등수가 더 높음
# 2. 동일한 경우 영어점수가 높을수록 등수 높음

n = int(input())
student = []
sorted_list = [0] * n

for i in range(n):
    math, eng = map(int, input().split())
    student.append((i+1, math, eng))


student.sort(key = lambda x: (-x[1],-x[2]))

for i in range(n):
    idx = student[i][0]
    # sorted_list의 index는 학생번호
    # 저장되는 값은 등수
    sorted_list[idx-1] = i+1

print(*sorted_list, sep="\n")    