N = int(input())
in1 = list(map(int, input().split()))

sum = 0
cnt = 0
for i in in1:
    if i == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)