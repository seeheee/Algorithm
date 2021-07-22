# 순열(메모리 초과 발생)
from itertools import permutations

g, s = map(int, input().split())
W = input()
S = input()
# 모든 순열을 리스트로 저장하면 안됨...
# permutation = list(map(''.join, permutations(W, g)))
#
# count = 0
# for per in permutation:
#     if per in S:
#         count += 1
#
# print(count)

wl = [0] * 52
sl = [0] * 52

for i in range(g):
    if 'a' <= W[i] <= 'z':
        wl[ord(W[i]) - ord('a')] += 1
    else:
        wl[ord(W[i]) - ord('A') + 26] += 1
print(wl)

start, length, count = 0, 0, 0

for i in range(s):
    if 'a' <= S[i] <= 'z':
        sl[ord(S[i]) - ord('a')] += 1
    else:
        sl[ord(S[i]) - ord('A') + 26] += 1
    length += 1
    print(length)

    if length == g:
        if wl == sl:
            count += 1
        if 'a' <= S[start] <= 'z':
            sl[ord(S[start]) - ord('a')] -= 1
        else:
            sl[ord(S[start]) - ord('A') + 26] -= 1
        start += 1
        length -= 1

print(count)