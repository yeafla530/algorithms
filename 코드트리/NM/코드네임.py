# class
class User:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score

n = 5
user = []
for _ in range(n):
    code_name, score = input().split()
    user.append(User(code_name, score))

min_score = 101
select = ''
for i in range(n):
    code = user[i].code_name
    score = int(user[i].score) 
    if min_score > score:
        min_score = score
        select = code

print(select, min_score)

# tuple
user = [tuple(input().split()) for _ in range(5)]

min_index = 0
for i in range(1, 5):
    _, min_score = user[min_index]
    _, score = user[i]

    min_score = int(min_score)
    score = int(score)


    if min_score > score:
        min_index = i

code, score = user[min_index]
print(code, score)
        
