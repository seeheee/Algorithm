N = int(input())

list1 = []
for i in range(N):
    in1 = input()
    list1.append(in1)

list2 = []
for j in list1:
    tmp = j.split('.')
    list2.append(tmp[1])

list2.sort()
print(list2)

count = 0
for k in range(len(list2)-1):
    if list2[k] == list2[k+1]:
        count += 1
    print(count)