N, K = map(int, input().split())

list1 = []
for i in range(1,N+1):
    if N % i == 0:
        list1.append(i)
    list1.sort()

if len(list1) < K:
    print("-1")

for i,j in enumerate(list1):
    if i+1 == K:
        print(j)




