N, M = map(int, input().split())

list1 = []
for k in range(N+M):
    in1 = input()
    list1.append(in1)

str_set = set()
for i in range(N):
    str_set.add(list1[i])

list2 = []
for j in range(N, len(list1)):
    list2.append(list1[j])

count = 0
for n in list2:
    if n in str_set:
        count += 1

print(count)
