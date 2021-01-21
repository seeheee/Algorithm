from functools import reduce
TC = int(input())

for _ in range(TC):
    N = int(input())
    list1 = []
    for _ in range(N):
        num1 = list(input().split())
        list1.append(num1[1])

        print(num1[1])


    dic = {}
    for i in list1:
        try:dic[i] += 1
        except:dic[i] = 1
    list2 = []
    for j in dic.values():
        list2.append(j)


    def multiply(list2):
        return reduce(lambda x, y: x * y, list2)

    print(multiply(list2))

