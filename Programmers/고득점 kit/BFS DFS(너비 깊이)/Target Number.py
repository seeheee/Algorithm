from itertools import product
def solution(numbers, target):
    list1 = [(i, -i) for i in numbers]
    answer = list(map(sum, product(*list1)))
    count = answer.count(target)
    return count