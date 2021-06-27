N = int(input())
list1 = list(map(int, input().split()))

average = round(sum(list1) / len(list1))

min = 2147000000
for idx, j in enumerate(list1):
    tmp = abs(j - average)
    if tmp < min:
        min = tmp
        score = j
        res = idx + 1
    elif tmp == min:
        if j > score:
            score = j
            res = idx + 1
print(average, res)



