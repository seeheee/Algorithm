def solution(N, stages):
    dic = {}
    fail = 0
    count = 0
    for i in range(1, N+2):
        dic[i] = 0
    for stage in stages:
        if stage not in dic:
            dic[stage] = 1
        else:
            dic[stage] += 1


    dic = sorted(dic.items(), key=lambda x: x[0])
    print(dic)
    value_list = []
    for d in range(len(dic)):
        tmp = dic[d][1]
        value_list.append(tmp)
    # print(value_list)

    answer = []
    for i in range(len(value_list)-1):
        fail = value_list[i] / sum(value_list[i+1:])
        # fail = value_list.pop(0) / sum(value_list)
        answer.append(fail)

    dic1 = {}
    for idx, v in enumerate(answer):
        dic1[idx+1] = v

    dic1 = sorted(dic1.items(), key=lambda x: x[1], reverse=True)
    # print(dic1)

    ha = []
    for j in range(len(dic1)):
        tmp1 = dic1[j][0]
        ha.append(tmp1)
    return ha

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

