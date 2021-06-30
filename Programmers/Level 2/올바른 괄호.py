# 하나도 막힘 없이 15분안에 풀었다 ㅎㅎ
def solution(s):
    s_list = list(map(str, s))
    stack = []
    for i in s_list:
        if len(stack) == 0:
            if i == '(':
                stack.append(i)
            else:
                return False
        elif stack[-1] == '(' and i == ')':
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        return True
    else:
        return False