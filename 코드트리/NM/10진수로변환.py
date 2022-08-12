# 화날뻔
binary = list(map(int, input()))
num = 0

for i in range(len(binary)):
    num = num * 2 + binary[i]
    
print(num)