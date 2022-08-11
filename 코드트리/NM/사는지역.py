class Person:
    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [Person(name, address, location) for name, address, location in arr]

target_idx = 0 
for i, person in enumerate(people):
    if person.name > people[target_idx].name:
        target_idx = i

print(f"name {people[target_idx].name}")
print(f"addr {people[target_idx].address}")
print(f"city {people[target_idx].location}")