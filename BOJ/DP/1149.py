import sys
input = sys.stdin.readline

N = int(input())

RGB = [list(map(int, input().rstrip().split())) for _ in range(N)]


D = [[0]*3 for _ in range(N)]


D[0][0] = RGB[0][0]
D[0][1] = RGB[0][1]
D[0][2] = RGB[0][2]

for i in range(1, N):
    D[i][0] = min(D[i-1][1], D[i-1][2]) + RGB[i][0]
    D[i][1] = min(D[i-1][0], D[i-1][2]) + RGB[i][1]
    D[i][2] = min(D[i-1][0], D[i-1][1]) + RGB[i][2]
    # print(D)
result = min({D[N-1][0], D[N-1][1], D[N-1][2]})
print(result)