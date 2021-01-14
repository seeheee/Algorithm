
w = []
for i in range(10):
    in1 = int(input())
    w.append(in1)

w.sort()

K=[]
for j in range(10):
    in2 = int(input())
    K.append(in2)

K.sort()

result1 = result2 = 0
for k in range(9, 6, -1):
    result1 += w[k]
    result2 += K[k]

print(result1, result2)
