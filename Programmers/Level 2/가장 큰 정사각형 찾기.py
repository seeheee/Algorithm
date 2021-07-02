# DP -> 2차원 배열이 입력으로 주어짐, 결과(최댓값, 최솟값), 방향이 정해져있다..
# answer에 담기는 거는 정사각형의 한 변의 길이 그러니깐 제곱

# o(n**2)
def solution(board):
    r = len(board)
    c = len(board[0])

    # 예외처리 필요([0,0][0,0] or [1,0][0,0])
    for b in board:
        if sum(b):
            answer = 1
            break
    else:
        return 0

    for i in range(1, r):  # 1부터 시작되는 이유는 0행
        for j in range(1, c):  # 0열은 고정적인 값이다.
            if board[i][j] == 1:
                board[i][j] = min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
                answer = max(answer, board[i][j])

    return answer ** 2

print(solution([[0,0], [1,0]]))