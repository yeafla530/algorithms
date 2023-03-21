arr = list(map(int, input().split()))



team1 = 0
team2 = 0
team3 = 0

max_cnt = 0
min_cnt = 987654321 
result = 987654321
for a in range(6):
    for b in range(6):
        if a == b:
            continue
        team1 = arr[a] + arr[b]
        for c in range(6):
            if c == a or c == b:
                continue
            
            for d in range(6):
                if d == a or d == b or d == c:
                    continue
                team2 = arr[c] + arr[d]
                
                team3 = sum(arr) - team1 - team2

                max_cnt = max(team1, team2, team3)
                min_cnt = min(team1, team2, team3)

                result = min(result, max_cnt-min_cnt)

print(result)

                