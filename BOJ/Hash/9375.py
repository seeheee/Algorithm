# dic 이용해서 푸는 거는 알겠는데 원하는 답을 얻기 위해서 어떻게 답을 해야하는지 몰랐음
TC = int(input())

for _ in range(TC):
    N = int(input())
    list1 = []
    for _ in range(N):
        num1 = list(input().split())
        list1.append(num1[1])

    dic = {}
    for i in list1:
        try:dic[i] += 1
        except:dic[i] = 1

    result = 1
    for k in dic:
        result *= dic[k] + 1

    print(result-1)



