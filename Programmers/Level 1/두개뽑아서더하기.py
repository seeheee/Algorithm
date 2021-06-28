from itertools import combinations

def solution(numbers):
    answer = sorted(list(set((map(sum, combinations(numbers, 2))))))
    return answer


# 더욱더 파이썬스럽게 짜기
def solution(numbers):
    return sorted(list(set([sum([i, j]) for i, j in combinations(numbers, 2)])))


print(solution([5,0,2,7]))