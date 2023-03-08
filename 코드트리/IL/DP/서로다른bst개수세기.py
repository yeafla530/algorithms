# BST = 자식을 2개 이하로 갖는 이진 탐색 트리
# 노드마다 왼쪽에 있는 모든 노드들의 값이 해당 노드의 값보다 작아야하고
# 오른쪽 있는 모든 노드들이 값이 해당 노드르이 값보다 커야함
MAX_INT = 19

n = int(input())
dp = [0] * (MAX_INT+1)

dp[0] = 1
dp[1] = 1

def get_num_of_unique_bst(n):
    num_of_unique_bst = 0

    # n = 4
    # root 1 : [] [2, 3, 4]
    # root 2 : [1] [3, 4]
    # root 3 : [1, 2] [3, 4]
    # root 4 : [1, 2, 3] [0] 

    for i in range(n):
        num_of_unique_bst += dp[i] * dp[n-i-1]
    
    return num_of_unique_bst

for i in range(2, n+1):
    dp[i] = get_num_of_unique_bst(i)

print(dp[n])

