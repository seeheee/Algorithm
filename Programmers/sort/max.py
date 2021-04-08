#### 시간초과 발생 이것을 어떻게 행어ㅏㅣㅣ#####
from itertools import permutations
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(str(i))

    result = list(map(''.join, permutations(answer, len(numbers))))
    result.sort(reverse=True)

    return result.pop(0)

############ 시간초과 발생 해결 #############


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key= lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))
