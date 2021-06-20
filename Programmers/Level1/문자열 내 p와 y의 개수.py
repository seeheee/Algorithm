s = "pPoooyY"
def solution(s):
    up_s = s.upper()
    # print(up_s)

    if up_s.count('P') == 0 and up_s.count('Y') == 0:
        return True
    elif up_s.count('P') == up_s.count('Y'):
        return True
    else:
        return False

# print(solution(s))