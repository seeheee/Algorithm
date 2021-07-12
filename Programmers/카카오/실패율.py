# 혼자 풀었어....
def solution(N, stages):
    dic = {}
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
    print(value_list)

    answer = []
    for i in range(len(value_list) - 1):
        # 이 예외처리가 어려웠음(오류: ZeroDivisionError: division by zero)
        # ex) 2/0
        current = sum(value_list[i + 1:])
        if current == 0:
            answer.append(value_list[i])
        else:
            fail = value_list[i] / sum(value_list[i + 1:])
            answer.append(fail)

    dic1 = {}
    for idx, v in enumerate(answer):
        dic1[idx+1] = v

    dic1 = sorted(dic1.items(), key=lambda x: x[1], reverse=True)
    print(dic1)

    final = []
    for j in range(len(dic1)):
        tmp1 = dic1[j][0]
        final.append(tmp1)
    return final


print(solution(4, [4,4,4,4,4]))

