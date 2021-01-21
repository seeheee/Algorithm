import sys
input = sys.stdin.readline

N = int(input())

list1 = []
for _ in range(N):
    num = input().rstrip()
    list1.append(num)


dic = {}

for j in list1:
    try: dic[j] += 1
    except: dic[j] = 0


list2 = []
for i,k in dic.items():
    if max(dic.values()) == k:
        list2.append(i)

list2.sort()

answer = list2[0]
print(answer)