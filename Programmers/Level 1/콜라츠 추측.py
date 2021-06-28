from collections import deque
def solution(num):
    visited = deque()
    answer = 0
    visited.append(num)
    while visited:
        num = visited.popleft()
        if num == 1:
            return answer
        if num % 2 == 0:
            visited.append(num // 2)
            answer += 1
        elif num % 2 == 1:
            visited.append((num * 3) + 1)
            answer += 1
        if answer == 500:
            return -1



print(solution(7))