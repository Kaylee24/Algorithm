import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order = input().strip()

    if 'push' in order:
        order, X = map(str, order.split())
        stack.append(int(X))
    elif order == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)