N = int(input())

result = 0
for i in range(N):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b == c:
        case = 10000 + (a * 1000)
    elif a == b or a == c:
        case = 10000 + (a * 100)
    elif b == c:
        case = 10000 + (b * 100)
    else:
        case = c * 100
    if case > result:
        result = case
print(result)