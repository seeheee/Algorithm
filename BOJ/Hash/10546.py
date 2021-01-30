import sys
import collections
input = sys.stdin.readline

N = int(input())

dic = {}
for i in range(N):
    in1 = input().rstrip()
    if in1 in dic:
        dic[in1] += 1
    else:
        dic[in1] = 1

for j in range(N-1):
    in2 = input().rstrip()
    if in2 in dic:
        result = dic[in2] - 1
        dic[in2] = result

for a, b in dic.items():
    if b >= 1:
        print(a)
