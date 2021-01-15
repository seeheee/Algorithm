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
count= {}
for k in list2:
    try:count[k] += 1
    except: count[k] = 1

for key, item in count.items():
    print(key, item)