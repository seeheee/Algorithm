N = int(input())
in1 = list(map(str, input().split()))

M = int(input())

in2 = list(map(str, input().split()))

result = []
for i in in1:
    result.append(int(i))

for j in in2:
    result.append(int(j))

result.sort()

for k in result:
    print(k, end=' ')