n = int(input())

students = []
for _ in range(n):
    name, height, weight = input().split()
    students.append((name, int(height), int(weight)))

students.sort(key=lambda x: (x[1], -x[2]))

for student in students:
    name, height, weight = student
    print(name, height, weight)