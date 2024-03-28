for _ in range(int(input())):
    bracket = list(input())

    stack = []
    P = True
    for b in bracket:
        if b == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                P = False
                break

    if P:
        if stack:
            print('NO')
        else:
            print('YES')