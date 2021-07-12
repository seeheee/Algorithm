# 맨 처음 방법인데 통과 못 함
from itertools import combinations
def solution(d, budget):
    for i in range(len(d), 0, -1):
        dList = list(combinations(d,i))
        for j in dList:
            if sum(j) == budget:
                return len(j)

# 그 금액보다 적은 금액 지원 못 해주면 딱 맞아야 하는거 아닌가?
# 왜..... 다시 풀기
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)




