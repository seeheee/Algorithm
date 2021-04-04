########### 에리토스테네스의 체를 이용하여 소수 구하기 ###########
n = 10
# 인덱스가 소수인 a 배열에서 0,1 빼고 True로 초기화
a = [False, False] + [True]*(n-1)

primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        # 배수 구하는것
        for j in range(2*i, n+1, i):
            a[j] = False
            print(a)
print(primes)
#######################################################

from itertools import permutations
pool = ['1', '5', '7']

print(list(map(''.join, permutations(pool, 2))))

#########################################################

from itertools import permutations
import math


def decimal(n):
    k = math.sqrt(n)
    if n < 2:
        return False
    for i in range(2, int(k) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    for i in range(1, len(numbers) + 1):
        result = set(map(int, map(''.join, permutations(numbers, i))))
        for j in result:
            if decimal(j):
                answer.append(j)
    return len(set(answer))





