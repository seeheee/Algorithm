# 에러발생
def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (solution(n - 1) + solution(n - 2)) % 1234567


def solution(n):
    answer = []
    for i in range(n + 1):
        if i < 2:
            answer.append(i)
        else:
            answer.append((answer[i - 1] + answer[i - 2]) % 1234567)
    return answer[-1]







