def f():
    N, K = map(int, input().split())
    board = [list(map(int, [*input()])) for _ in range(2)]

    queue = [(0, 0, 0)]
    result = 0

    while queue:
        i, j, t = queue.pop(0)
        if i+K >= N:
            result = 1
            break

        if board[1-j][i+K]:
            queue.append((i+K, 1-j, t+1))
            board[1-j][i+K] = 0
        if board[j][i+1]:
            queue.append((i+1, j, t+1))
            board[j][i+1] = 0
        if i-1 > t and board[j][i-1]:
            queue.append((i-1, j, t+1))
            board[j][i-1] = 0

    print(result)

f()
