TC = int(input())

D = [0 for _ in range(15)]

D[1] = 1
D[2] = 2
D[3] = 4
for _ in range(TC):
    in1 = int(input())
    for i in range(4, in1+1):
        D[i] = D[i-1] + D[i-2] + D[i-3]
    print(D[in1])