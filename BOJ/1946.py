N = int(input())
in1 = [list(map(int, input().split())) for _ in range(N)]

in1.sort(key=lambda x:x[0])

print(in1)

result = []
for i in range(1,N):
    for j in range(2):
        if in1[0][1] > in1[i][1]:
            result.append([in1[i][j]])

print(result)








