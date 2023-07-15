# Y 2, F 3, O 4
# 플레이 신청횟수 N과 임스와 플레이할 게임 종류 주어짐
# 최대 몇번이나 임스와 함께 할 수 있는지
# 몇번이나 미니 게임을 플레이할 수 있는지

# 한번 플레이한 사람과는 다시 플레이하지 않음

# 내 풀이 - 시간 초과 
# n, play = input().split()
# n = int(n)
# already = []
# ans = 0
# cnt = 0

# for i in range(n):
#     player = input()

#     if player not in already:
#         cnt +=1
    
#     if play == "Y" and cnt == 1:
#         ans += 1
#         cnt = 0
#     elif play == "F" and cnt == 2:
#         ans += 1
#         cnt = 0
    
#     elif play == "O" and cnt == 3:
#         ans += 1
#         cnt = 0
    
#     if player not in already:
#         already.append(player)


# print(ans)

# 정답 풀이
d = {"Y": 1, "F": 2, "O": 3}
n, play = input().split()
player = [input() for _ in range(int(n))]
player = list(set(player))

ans = len(player) // d[play]

print(ans)
