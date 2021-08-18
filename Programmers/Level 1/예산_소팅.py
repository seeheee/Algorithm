def solution(d, budget):
    d.sort()

    answer = 0

    for i in d:
        budget = budget - i
        if budget < 0:
            break
        answer += 1
    return answer

print(solution([1,3,2,5,4],	9))