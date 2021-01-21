
case = int(input())

for _ in range(case):
    N = int(input())
    num1 = map(int, input().split())
    M = int(input())
    num2 = list(map(int, input().split()))

    dic = {}
    for ob in num1:
        dic[ob] = 0

    print(dic)

    for i in num2:
        if i not in dic.keys():
            print(0)
        else:
            print(1)