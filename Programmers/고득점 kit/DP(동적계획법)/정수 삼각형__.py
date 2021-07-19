# 메모리제이션 기법
dic = {1: 1, 2: 1}

def fib_memoization(n):
    if n in dic:
        return dic[n]

    dic[n] = fib_memoization(n - 1) + fib_memoization(n - 2)
    print(dic)
    return dic[n]


print(fib_memoization(5))

# 풀이... 이런생각을 어떻게 하지..? 너무 어려움
def solution(triangle):
    triangle = [[0] + line + [0] for line in triangle] # 0은 다음번째 배열에서 최대값을 담기위해서 index 예외를 막는 방법

    for i in range(1, len(triangle)):
        for j in range(1, i+2): # 하나씩 최대값을 구해야하는 숫자의 개수가 늘어나니까는 +2를 해 주는거(맨 마지막은 안 들어감)
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    return max(triangle[-1])  # 항상 DP에서는 가장 마지막 값이 내가 구하려는 답

