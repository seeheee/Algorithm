# 1로 만들기 2

in1 = int(input())

D = [0 for _ in range(1000005)]

D[0] = 0

for i in range(1, in1+1):
    D[i] = D[i-1] + 1
    if i % 3 == 0:
        D[i] = D[i // 3] + 1
    if i % 2 == 0:
        D[i] = D[i // 2] + 1
    print("D[i]", D[i], i)
print(D[in1])