n = int(input())
students = []
for i in range(n):
    t, w = map(int, input().split())
    students.append((t, w, i+1))

students.sort(key=lambda x: (-x[0], -x[1], x[2]))
for student in students:
    t, w, i = student
    print(t, w, i)