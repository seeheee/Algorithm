# 0,0,0이 들어올 경우 "000"이 아니고 "0"이니깐 int형으로 바꿔주어야 함
# 숫자의 문자형의 아스키코드 이용

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 1000, reverse=True)

    return str(int(''.join(numbers)))
