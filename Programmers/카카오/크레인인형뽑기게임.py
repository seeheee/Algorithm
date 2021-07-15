def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for j in range(len(board)):
            print(j, i)
            if board[j][i - 1] != 0:
                stack.append(board[j][i - 1])
                board[j][i - 1] = 0
                break
            else:
                pass

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 1

    return answer * 2


# 내 코드
def solution(board, moves):
    stack = []
    answer = 0
    while moves:
        move = moves.pop(0)
        for i in board:
            if i[move - 1] != 0:
                stack.append(i[move - 1])
                i[move - 1] = 0
                break

        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 1
    return answer * 2