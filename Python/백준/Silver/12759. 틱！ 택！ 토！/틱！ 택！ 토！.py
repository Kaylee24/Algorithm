first = int(input())
board = [[2] * 3 for _ in range(3)]

for _ in range(9):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    winner = 0

    # Set the board based on the player
    if first == 1:
        board[x][y] = 1
    else:
        board[x][y] = 0

    # Checking for winning conditions
    result = []
    for i in range(3):
        result.append([board[i][0], board[i][1], board[i][2]])  # Rows
        result.append([board[0][i], board[1][i], board[2][i]])  # Columns

    # Diagonals
    result.append([board[0][0], board[1][1], board[2][2]])
    result.append([board[0][2], board[1][1], board[2][0]])

    # Check for a winner
    if [1, 1, 1] in result:
        winner = 1
    elif [0, 0, 0] in result:
        winner = 2

    # If no winner, check for a draw
    if winner == 0:
        flag = False
        for line in result:
            if 2 in line:
                flag = True
                break
        if not flag:
            winner = 3  # Draw

    # End the game if there's a winner or a draw
    if winner > 0:
        break

    # Switch turns
    if first == 1:
        first = 2
    else:
        first = 1

# Print the result
if winner < 3:
    print(winner)
else:
    print(0)
