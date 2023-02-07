n = int(input())



a = ord('A')
for i in range(n):
    
    for j in range(i):
        print(" ", end=" ")
    for j in range(n-i):
        if a > ord('Z'):
            a = ord('A')
        print(chr(a), end=" ")
        a += 1
    
    
    print()