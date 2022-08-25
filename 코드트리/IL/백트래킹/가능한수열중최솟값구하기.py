import sys

n = int(input())
arr = [4, 5, 6]
box = []

# 인접한 수가 없는지 확인하는 함수
def possible():
    # 점점 늘려나감
    length = 1
    idx = len(box)
    while True:
        # 맨 끝부터 시작
        s1, e1 = idx - length, idx -1
        # s2의 시작점이 0보다 작으면 안됨
        s2, e2 = s1 - length, s1-1

        if s2 < 0:
            break

        
        if box[s1:e1+1] == box[s2:e2+1]:
            return False
        
        length += 1
    # 끝까지 돌았을 때 부분 수열 없으면 True
    return True

# 수열 뽑기
def choose(cnt):
    if cnt == n:
        for elem in box:
            print(elem, end="")
        sys.exit(0)

    for i in range(3):
        box.append(arr[i])
        # 중간에 검수
        if possible():
            choose(cnt+1)
        box.pop()

    

choose(0)

# 시간 초과
import sys

n = int(input())
arr = [4, 5, 6]
box = []

# 인접한 수가 없는지 확인하는 함수
def possible():
    for idx in range(len(box)):
        # 점점 늘려나감
        length = 1
        while True:
            s1, e1 = idx, idx + length -1
            s2, e2 = e1 + 1, (e1+1) + length -1

            if e2 >= len(box):
                break
            
            if box[s1:e1+1] == box[s2:e2+1]:
                return False
            
            length += 1
    # 끝까지 돌았을 때 부분 수열 없으면 True
    return True

# 수열 뽑기
def choose(cnt):
    if cnt == n:
        if possible():
            for elem in box:
                print(elem, end="")
            sys.exit(0)
        return
    for i in range(3):
        box.append(arr[i])
        choose(cnt+1)
        box.pop()

    

choose(0)