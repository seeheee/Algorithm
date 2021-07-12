# 아이디어는 맞았는데 정규표현식을 어떻게 작성해야 하는지 막힘...
import re

def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}

    dartSet = re.compile('(\d+)([SDT])([*#]?)').findall(dartResult)
    # 	[('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]
    for d in range(len(dartSet)):
        if dartSet[d][2] == '*' and d > 0: # 2배처리해주는 예외가 까다로움
            dartSet[d - 1] *= 2
        # dartSet[d] 이렇게 계산한 값을 바꿔주는 생각을 아예 못함
        dartSet[d] = int(dartSet[d][0]) ** bonus[dartSet[d][1]] * option[dartSet[d][2]]
        print(dartSet)

    answer = sum(dartSet)
    return answer

print(solution("1D#2S*3S"))