# 효율성 통과 못 함
def solution(s):
    s_list = list(map(str, s))
    stack = []
    while s_list:
        if stack: # 스택이 없는 경우를 만들어줘야 인덱스 오류 안남(맨 처음 부분이랑, s_list는 남았는데 스택이 비어있어 stack[-1]에서 오류남
            if stack[-1] == s_list[0]:
                s_list.pop(0)
                stack.pop()
            else:
                stack.append(s_list.pop(0))
        else:
            stack.append(s_list.pop(0))

    if len(stack) == 0:
        return 1
    else:
        return 0



# 효율성도 통과한 코드
# s를 굳이 리스트로 넣을 필요가 없음
def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if len(stack) == 0:
        return 1
    else:
        return 0


def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if stack:
        return 0
    else:
        return 1

print(solution("cdcd"))