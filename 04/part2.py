board = []

file_name = "sample.txt"
file_name = "data.txt"


def check_xmas(board, x, y) -> int:
    valid_chars = ["M", "S"]
    if x - 1 >= 0 and y - 1 >= 0 and x + 1 < len(board) and y + 1 < len(board[x]):
        if (
            board[x - 1][y - 1] == board[x - 1][y + 1]
            and board[x + 1][y + 1] == board[x + 1][y - 1]
            and board[x - 1][y - 1] != board[x + 1][y + 1]
            and board[x - 1][y - 1] in valid_chars
            and board[x + 1][y + 1] in valid_chars
        ) or (
            board[x - 1][y + 1] == board[x + 1][y + 1]
            and board[x + 1][y - 1] == board[x - 1][y - 1]
            and board[x - 1][y + 1] != board[x + 1][y - 1]
            and board[x - 1][y + 1] in valid_chars
            and board[x + 1][y - 1] in valid_chars
        ):
            return 1

    return 0


with open(file_name, "r") as file:
    file_data = file.read().split("\n")
    for line in file_data:
        board.append(list(line))

xmas_count = 0
for x in range(len(board)):
    for y in range(len(board)):
        if board[x][y] == "A":
            xmas_count += check_xmas(board, x, y)

print(xmas_count)
