# def solution(s):
#     stack = []
#     for char in s:
#         if stack and char > stack[-1]:
#             stack.pop()
#         stack.append(char)
#
#     return ''.join(stack)



def solution(s):
    stack = []
    for char in s:
        while stack and char > stack[-1]:
            stack.pop()
        stack.append(char)

    return ''.join(stack)


print(solution("acbcdd"))