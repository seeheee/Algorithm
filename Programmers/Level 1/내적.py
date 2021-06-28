
a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]


# 리스트에서 sum 쓰면 가능
# sum(iterable) - iterable한 자료형을 받으며 numeric 해야합니다.
# 즉, 리스트나 튜플 처럼 인덱스 순환 접근이 가능한 자료형이고 내부에 숫자로만 이루어져 있어야합니다.
# 여기서 숫자는 정수, 실수 둘다 가능입니다

def solution(a, b):
    # answer = 0
    return sum(list(map(lambda x, y: x*y, a, b)))




def solution(a, b):
    answer = 0
    list1 = list(map(lambda x, y: x*y, a, b))
    for i in list1:
        answer += i
    return answer

print(solution(a,b))