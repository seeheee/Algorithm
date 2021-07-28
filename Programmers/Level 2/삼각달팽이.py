
def solution(n):
    answer = [[] for _ in range(n + 1)]
    for i in range(1, 1000):
        answer[i].append(i)
        while len(answer[n]) == n:
            answer[n].append(i)
        print(answer)

print(solution(4))