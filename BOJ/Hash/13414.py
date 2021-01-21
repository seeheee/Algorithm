# 시간초과 해결방법을 못 찾겠음


import sys
import collections
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())


list1 = []
for _ in range(M):
    num = input().rstrip()
    list1.append(num)

# dic = {}
# for j in list1:
#     try: dic[j] += 1
#     except: dic[j] = 1
#

a = collections.Counter(list1)

list2 = []
for i,k in a.items():
    if k >= 2:
        list2.append(i)


for m in list2:
    if m in list1:
        list1.remove(m)

answer = list1[:N]

for i in answer:
    print(i)

