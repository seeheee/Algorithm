# 총 15개 테케 중에서 8개 시간초과 나머지는 통과
# 혼자 풀었는데 시간초과 발생해서 아쉽
import re
def solution(s):
    dic = {}
    answer = []
    s = s.replace("{", "")
    s = s.replace("}", "")

    # s1방법보다 s가 깔끔
    s1 = re.compile('(\D)').split('' + s)
    s = s.split(',')

    # 시간초과 발생 주요 원인
    # for i in s:
    #     dic[i] = s.count(i)

    for i in s1:
        # if i == ',':
        #     continue
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    for i in range(len(dic)):
        answer.append(int(dic[i][0]))

    return answer


print(solution("{{20,111},{111}}"))