# 기능 개발

# 1일때 밖에서 넣는거를 생각못했다. break를 통해서
import math
from collections import deque
def solution(progresses, speeds):
    days = deque()
    answer = []
    for i in range(len(progresses)):
        day = (100- progresses[i]) / speeds[i]
        days.append(math.ceil(day))

    while days:
        count = 1
        a = days.popleft()
        days1 = days.copy()
        for j in range(len(days)):
            if a < days[j]:
                break
            else:
                days1.popleft()
                count += 1
        answer.append(count)
        days = days1.copy()
    return answer