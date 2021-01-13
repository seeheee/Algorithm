
N = int(input())

largest = -2147000000

# 2차원 리스트 만들기
list1 = [list(map(int, input().split())) for _ in range(N)]

largest = -2147000000
for i in range(N):
    row = col = 0
    for j in range(N):
        row += list1[i][j]
        col += list1[j][i]
    if row > largest:
        largest = row
    elif col > largest:
        largest = col


sum1 = sum2 = 0
for n in range(N):
    for m in range(N, -1, -1):
        print(m)
        if n == m:
            sum1 += list1[n][m]
        elif n + m == N-1:
            sum2 += list1[n][m]

result = []
result.append(sum1)
result.append(sum2)
result.append(largest)

print(max(result))
