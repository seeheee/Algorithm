N, M = map(int, input().split())

list1=[]
for i in range(N+M):
    in1 = input()
    list1.append(in1)

list1.sort()

count = 0
word = []
for j in range(len(list1)-1):
    if list1[j] == list1[j+1]:
        count += 1
        word.append(list1[j])

print(count)
for k in word:
    print(k)
