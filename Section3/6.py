import math

N = int(input())

in1 = [list(map(int, input().split())) for _ in range(N)]

sum1 = 0
for i in range(N):
    for j in range(N):
        if i == 0 and math.floor(N/2) == j:
            sum1 += in1[i][j]

