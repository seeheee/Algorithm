#### 시간초과 #####
from itertools import permutations
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(str(i))

    result = list(map(''.join, permutations(answer, len(numbers))))
    result.sort(reverse=True)

    return result.pop(0)