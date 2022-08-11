class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
# student = [Student(name, int(kor), int(eng), int(math)) for name, kor, eng, math in arr]

# student.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

# for s in student:
#     print(s.name, s.kor, s.eng, s.math)

arr.sort(key=lambda x: (-int(x[1]), -int(x[2]), -int(x[3])))
for a in arr:
    name, kor, eng, math = a
    print(name, kor, eng, math)