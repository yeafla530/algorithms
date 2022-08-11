students = []
for _ in range(5):
    name, height, weight = input().split()
    students.append((name, int(height), float(weight)))

students.sort(key=lambda x: x[0])
print("name")
for student in students:
    name, height, weight = student
    print(name, height, weight)

print()
students.sort(key=lambda x: -x[1])
print("height")
for student in students:
    name, height, weight = student
    print(name, height, weight)
