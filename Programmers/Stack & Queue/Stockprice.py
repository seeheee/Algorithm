# 주식가격
# 알고리즘 설명
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