# 주식가격
from collections import deque 
def solution(prices):
    que = deque()
    cnt = 1
    for i in range(prices):
        if prices[i] < prices[i+1]:
            cnt += 1
        else:
            que.insert(prices[i])
        print(que)
    answer = []
    return answer