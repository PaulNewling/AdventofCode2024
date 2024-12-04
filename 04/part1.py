board = []

file_name = "sample.txt"
file_name = "data.txt"


def check_xmas(board, x, y) -> int:
    count = 0
    search = "XMAS"

    # check up
    i = 0
    while x - i >= 0 and i < len(search):
        if board[x - i][y] != search[i]:
            break
        i += 1
    if i == len(search):
        count += 1
    # check down
    i = 0
    while x + i < len(board) and i < len(search):
        if board[x + i][y] != search[i]:
            break
        i += 1
    if i == len(search):
        count += 1

    # check left
    i = 0
    while y - i >= 0 and i < len(search):
        if board[x][y - i] != search[i]:
            break
        i += 1
    if i == len(search):
        count += 1
    # check right
    i = 0
    while y + i < len(board[x]) and i < len(search):
        if board[x][y + i] != search[i]:
            break
        i += 1
    if i == len(search):
        count += 1

    # check down left
    i = 0
    while x + i < len(board) and y - i >= 0 and i < len(search):
        if board[x + i][y - i] != search[i]:
            break
        i += 1
    if i == len(search):
        count += 1
    # check down right
    i = 0
    while x + i < len(board) and y + i < len(board[x]) and i < len(search):
        if board[x + i][y + i] != search[i]:
            break
        i += 1
    if i == len(search):
        count += 1

    # check up left
    i = 0
    while x - i >= 0 and y - i >= 0 and i < len(search):
        if board[x - i][y - i] != search[i]:
            break
        i += 1
    if i == len(search):
        count += 1
    # check up right
    i = 0
    while x - i >= 0 and y + i < len(board[x]) and i < len(search):
        if board[x - i][y + i] != search[i]:
            break
        i += 1
    if i == len(search):
        count += 1

    return count


with open(file_name, "r") as file:
    file_data = file.read().split("\n")
    for line in file_data:
        board.append(list(line))

xmas_count = 0
for x in range(len(board)):
    for y in range(len(board)):
        if board[x][y] == "X":
            xmas_count += check_xmas(board, x, y)

print(xmas_count)
