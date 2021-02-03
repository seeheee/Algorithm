import sys
input = sys.stdin.readline
N, M = map(int, input().split())
D = [0 for _ in range(N)]

arr = list(map(int, input().rstrip().split()))

# print(arr)

D[0] = arr[0]

for i in range(1, N):
    D[i] = D[i-1] + arr[i]
# print(D)


for j in range(M):
    start, end = map(int, input().split())
    if start == 1:
        result = D[end-1]
    else:
        result = D[end-1] - D[start - 2]
    print(result)