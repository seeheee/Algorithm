def solution(board, nums):
    row, col, dia = [0] * len(board), [0] * len(board), [0] * 2

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] in nums:
                row[i] += 1
                col[i] += 1
                if i == j:
                    dia[0] += 1
                if i + j == len(board) - 1:
                    dia[1] += 1

    r = row.count(len(board))
    c = col.count(len(board))
    d = dia.count(len(board))

    return r + c + d
