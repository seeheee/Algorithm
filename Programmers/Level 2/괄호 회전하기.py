from collections import deque
def solution(s):

    def check(x):
        stack = []
        for i in range(len(x)):
            if stack and stack[-1] == '[' and x[i] == ']':
                stack.pop()
            elif stack and stack[-1] == '(' and x[i] == ')':
                stack.pop()
            elif stack and stack[-1] == '{' and x[i] == '}':
                stack.pop()
            else:
                stack.append(x[i])

        if not stack:
            return 1

    s = deque(s)
    answer = 0
    for _ in range(len(s)):
        s.rotate(-1)
        if check(s):
            answer += 1
    return answer


# 함수 만들지 않고 풀기
from collections import deque

def solution(s):
    s = deque(s)
    answer = 0

    for _ in range(len(s)):
        s.rotate(-1)
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == '[' and s[i] == ']':
                stack.pop()
            elif stack and stack[-1] == '(' and s[i] == ')':
                stack.pop()
            elif stack and stack[-1] == '{' and s[i] == '}':
                stack.pop()
            else:
                stack.append(s[i])

        if not stack:
            answer += 1

    return answer