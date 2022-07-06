# ???

num, hp = map(int, input().split())
monster = list(map(int, input().split()))
people = list(map(int, input().split()))
result = 0

join = zip(monster, people)
join = list(join)


join.sort(key=lambda x : x[0])



for i in range(len(join)) :
    hp -= join[i][0]
    if (hp >= 0):
        result += join[i][1]
    else:
        print(result)
        break
