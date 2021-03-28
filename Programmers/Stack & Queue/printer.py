# 프린터
priorities = [1,1,9,1,1,1]
location = 0
from collections import deque

# 최대값이 index에서 첫번째 일 경우 storage를 조절하는 것이 어려움
def solution(priorities, location):
    storage = [j for j in range(len(priorities))]
    while priorities:
        a = priorities.pop(0)
        priorities1 = priorities.copy()
        for i in range(len(priorities)):
            if a < priorities[i]:
                priorities1.append(priorities1.pop(0))
                storage.append(storage.pop(0))
            else:
                if a == max(priorities):
                    priorities1.pop(0)

        priorities = priorities1.copy()
    for q in range(len(storage)):
        if location == storage[q]:
            answer = q + 1
    return answer


# 올바른 답
def solution(priorities, location):
    storage = [j for j in range(len(priorities))]
    priorities1 = priorities.copy()

    i = 0
    while True:
        if priorities1[i] < max(priorities1[i + 1:]):
            priorities1.append(priorities1.pop(i))
            storage.append(storage.pop(i))
        else:
            i += 1

        if priorities1 == sorted(priorities1, reverse=True):
            break
    for q in range(len(storage)):
        if location == storage[q]:
            answer = q + 1
    return answer

print(solution(priorities, location))