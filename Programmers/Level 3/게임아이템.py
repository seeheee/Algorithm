import heapq
from collections import deque

# item 체력이 적은순으로 정렬, 그냥 체력이 적은 순으로 하나씩 비교하는거는 맞음

def solution(healths, items):
    tmp = []
    for idx, item in enumerate(items):
        tmp.append((*item, idx))
    items = sorted(tmp, key=lambda x: x[1])
    items = deque(items)

    answer = []
    cand = []
    healths.sort()
    for health in healths:
        while items and health - items[0][1] >= 100:
            attack, power, idx = items.popleft()
            heapq.heappush(cand, (-attack, idx))
        if cand:
            c = heapq.heappop(cand)
            answer.append(c[1] + 1)
        answer.sort()
    return answer


# print(solution([200,120,150], [[30,100],[500,30],[100,400]]))