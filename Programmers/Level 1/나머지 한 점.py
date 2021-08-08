def solution(v):
    x_list = []
    y_list = []
    stack = []
    y_stack = []

    for i, j in v:
        x_list.append(i)
        y_list.append(j)

    x_list.sort()
    y_list.sort()

    while x_list:
        num = x_list.pop()
        if not stack:
            stack.append(num)
        else:
            if stack[-1] == num:
                stack.pop()
            else:
                stack.append(num)

    while y_list:
        num = y_list.pop()
        if not y_stack:
            y_stack.append(num)
        else:
            if y_stack[-1] == num:
                y_stack.pop()
            else:
                y_stack.append(num)

    return [stack[0], y_stack[0]]


# def solution(v):
#     x_list = []
#     y_list = []
#     stack = []
#     y_stack = []
#
#     for i, j in v:
#         x_list.append(i)
#         y_list.append(j)
#
#     x_list.sort()
#     y_list.sort()
#
#     while x_list:
#         num = x_list.pop()
#         if not stack:
#             stack.append(num)
#         else:
#             if stack[-1] == num:
#                 stack.pop()
#             else:
#                 stack.append(num)
#
#     while y_list:
#         num = y_list.pop()
#         if not y_stack:
#             y_stack.append(num)
#         else:
#             if y_stack[-1] == num:
#                 y_stack.pop()
#             else:
#                 y_stack.append(num)
#
#     return [stack[0], y_stack[0]]

print(solution([[1, 4], [3, 4], [3, 10]]))