class Info:
    def __init__(self, name, tall, age):
        self.name = name
        self.tall = tall
        self.age = age

n = int(input())

arr = [tuple(input().split()) for _ in range(n)]
# arr.sort(key=lambda x: int(x[1]))

# for name, tall, age in arr:
#     print(name, tall, age) 

info = [Info(name, tall, age) for name, tall, age in arr]
# print(info)
info.sort(key=lambda x: int(x.tall))

for i in info:
    print(i.name, i.tall, i.age)

