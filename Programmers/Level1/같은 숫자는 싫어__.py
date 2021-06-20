from collections import deque
arr = [4,4,4,3,3]

def solution(arr):
    stack = []
    stack.append(arr.pop(0))
    while arr:
        if stack[-1] == arr[0]:
            arr.pop(0)
            stack.append(arr.pop(0))
        else:
            stack.append(arr[0])
    return stack

print(solution(arr))