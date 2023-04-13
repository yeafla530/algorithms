n, m = map(int, input().split())

# 2차원 리스트로 받기
dna = []

for _ in range(n):
    dna.append(list(input()))

# print(n, m)

# 가능한 모든 부분 집합
supperDNA = [None for _ in range(2**n)]
supperDNA[0] = ['.'] * m

print(supperDNA)

# 두 염기서열을 합친다
def merge(dna1, dna2):
    # 합칠 수 없는 염기서열 = Null list
    if dna1 == [] or dna2 == []:
        return []

    dna = []
    for i in range(m):
        if dna1[i] == '.':
            dna.append(dna2[i])
        elif dna2[i] == '.':
            dna.append(dna1[i])
        elif dna1[i] == dna2[i]:
            dna.append(dna1[i])
        else:
            return []
    
    return dna


def genSupperDNA(index):
    loc = 0
    tempIndex = index
    while tempIndex % 2 == 0:
        tempIndex = tempIndex//2
        loc += 1

    supperDNA[index] = merge(dna[loc], supperDNA[index-2**loc])        


for i in range(1, 2**n):
    genSupperDNA(i)

print(supperDNA)