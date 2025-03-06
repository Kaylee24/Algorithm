for _ in range(int(input())):
    C = int(input())
    result = []
    
    result.append(C//25)
    C %= 25
    result.append(C//10)
    C %= 10
    result.append(C//5)
    C %= 5
    result.append(C)
    
    print(*result)