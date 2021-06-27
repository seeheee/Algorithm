N = int(input())
in1 = list(map(int, input().split()))

def digit_sum(x):
    add = 0
    tmp = str(i)
    for j in tmp:
        add = add + int(j)
    return add

max1 = -2147000000
for i in in1:
    tot = digit_sum(i)
    if tot > max1:
        max1 = tot
        result = i

print(result)



