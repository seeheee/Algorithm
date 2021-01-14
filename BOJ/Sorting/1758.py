N = int(input())

in1 = []
for i in range(N):
    in1.append(int(input()))

in1.sort(reverse=True)

result = []
for idx, j in enumerate(in1):
    value = j - idx
    if value > 0:
        result.append(value)

sum1 = 0
for k in result:
    sum1 += k
print(sum1)