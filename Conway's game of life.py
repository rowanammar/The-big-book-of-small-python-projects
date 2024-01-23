import time, os

board = [[False for _ in range(100)] for _ in range(18)]


def CountTrueNeighbors(matrix, row, col):
    rows, cols = 18, 100
    count = 0
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col) and matrix[i][j]:
                count += 1
    return count


def game():
    new_board = [[False for _ in range(100)] for _ in range(18)]
    for row in range(0, 18):
        for column in range(0, 100):
            neighbors = CountTrueNeighbors(board, row, column)

            if (neighbors in (2, 3)) and board[row][column]:
                new_board[row][column] = True
            elif neighbors == 3 and not board[row][column]:
                new_board[row][column] = True
            else:
                new_board[row][column] = False

    # Update the original board with the new values
    for row in range(0, 18):
        for column in range(0, 100):
            board[row][column] = new_board[row][column]


board[2][2] = board[2][3] = board[3][2] = board[3][1] = board[4][2] = 1
while True:
    game()
    for row in board:
        print(''.join('-' if not cell else '*' for cell in row))
    time.sleep(0.5)
    if not any(any(row) for row in board):
        break
    os.system('cls')
