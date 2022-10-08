T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    number = list(input())
    num_list = set()
    l = n // 4
    for i in range(l):
        for j in range(4):
            num_list.add(int(''.join(number[j * l: (j + 1) * l]), 16))
        number.append(number.pop(0))
    final = sorted(list(num_list), reverse=True)[k - 1]
    print('#{} {}'.format(test_case, final))

# 초기 상태 pos, state 정의
# pos[i] : 매 상태에서 3 * 3 * 3에서 순서대로 넘버링했을 때, i번쨰 큐브의 번호
# state[i] : 초기 i번 큐브의 상태
def init():
    pos, state = [i for i in range(27)], [
        [0 for _ in range(6)] for i in range(27)]
    for idx, col in enumerate('wyrogb'):
        for block in side[idx]:
            state[block][idx] = col
    return pos, state


def process():
    N = input()
    # 회전 별로 pos, state 변경
    pos, state = init()  # 초기화
    for order in input().split():
        pos, state = rotate(order, pos, state)

    # 윗면 큐브들에서 위만 출력
    for i, idx in enumerate(side[0]):
        print(state[pos[idx]][0], end=''+(i % 3 == 2)*'\n')

# Main 함수
if __name__ == '__main__':
    # 테스트 케이스 별 과정 진행
    TC = int(input())
    for _ in range(TC):
        process()