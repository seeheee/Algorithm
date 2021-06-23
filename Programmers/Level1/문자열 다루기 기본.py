def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False  # 예외처리 해 줘야함(문제에는 없었음)



print(solution("1234"))