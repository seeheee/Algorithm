from itertools import combinations


def solution(m, weights):
    answer = 0
    for i in range(len(weights)):
        cand = list(map(sum, combinations(weights, i + 1)))

        for c in cand:
            if c == m:
                answer += 1
    return answer