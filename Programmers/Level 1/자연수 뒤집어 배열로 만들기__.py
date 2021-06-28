# 1234567890 일 경우 못 함
def solution(n):
    answer = list(map(int, str(n)))
    answer.sort(reverse=True)
    return answer

# 가능하게 만들기

print(solution(12334567890))