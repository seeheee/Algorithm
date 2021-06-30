def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    answer = sum(i * j for i, j in zip(A, B))
    return answer