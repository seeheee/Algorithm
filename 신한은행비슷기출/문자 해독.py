# 순열(메모리 초과 발생)
from itertools import permutations

g, s = map(int, input().split())
W = input()
S = input()

permutation = list(map(''.join, permutations(W, g)))

count = 0
for per in permutation:
    if per in S:
        count += 1

print(count)

# 모든 순열을 리스트로 저장하면 안됨...
