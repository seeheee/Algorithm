N, M = map(int, input().split())

result = []
for i in range(1,N+1):
    for j in range(1,M+1):
        sum = i + j
        result.append(sum)
        result.sort()

w_count = {}
for k in result:
    try: w_count[k] += 1
    except: w_count[k] = 1


max = -2147000000
for n in w_count.keys():
    if w_count[n] > max:
        max = w_count[n]

for m in w_count.keys():
    if w_count[m] == max:
        print(m, end=' ')
