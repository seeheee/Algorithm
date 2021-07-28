# 당연히 DP인줄 알았는데 DP로 풀면 시간초과 생김
def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            answer += 1
    return answer