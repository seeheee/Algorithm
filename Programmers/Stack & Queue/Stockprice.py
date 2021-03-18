# 주식가격
from collections import deque
def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    stack = [0]
    for i in range(1, len(prices)):
        while stack:
            idx = stack[-1]
            if prices[idx] > prices[i]:
                answer[idx] = i - idx
                stack.pop()
            else:
                break
        stack.append(i)
    return answer