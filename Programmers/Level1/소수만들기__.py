from itertools import combinations
import math

nums = [1, 2, 7, 6, 4]

math.sqrt(11)
# 3.3166247903554
print(int(math.sqrt(11)))
# 3

# 소수 판별 함수
# 소수란 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수
def is_prime_number(n):
    if n == 0 and n == 1: # 1보다 큰 자연수이므로 0과 1이 들어올 수 없음
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1): # 약수만 나누어질수 있으므로 약수의 제곱근까지만 봐서 판별
            if n % i == 0:
                return False
        return True


def solution(nums):
    answer = 0
    com_tuple = list(combinations(nums, 3)) # nums의 원소가 문자가 아니라 숫자일 경우는 바로 조합 사용 가능
    for ct in com_tuple:
        if is_prime_number(sum(ct)):
            answer += 1
    return answer


print(solution(nums))