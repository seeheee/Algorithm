N, K = map(int, input().split())

result = set()
for i in range(N):
    a = list(map(int, input().split()))
    a.sort(reverse=True)

for j in a:
    result.add(j)

for k in result:
    


