from itertools import combinations
from itertools import permutations, combinations
import re


def solution(expression):
    expressions = set(re.findall("\D", expression))
    priorty = permutations(expressions)
    answer = []

    for p in priorty:
        tmp1 = list(map(str, expression))
        tmp = re.compile("(\D)").split('' + expression)
        # print(tmp)
        # print(tmp1)
        for s in p:
            while s in tmp:
                index = tmp.index(s)
                tmp = tmp[:index-1] + [str(eval(''.join(tmp[index-1:index+2])))] + tmp[index+2:]
        answer.append(abs(int(tmp[0])))
        print("real", answer)
    return max(answer)

print(eval("3+6"))
from itertools import permutations
import re


def solutiosn(expression):
    expressions = set(re.findall('\D', expression))
    prior = permutations(expressions)
    answer = []

    for p in prior:
        # 기호를 공백으로 만든 다음 문자열을 합친다.
        tmp = re.compile('(\D)').split('' + expression)
        for s in p:
            if s in tmp:
                index = tmp.index(s)
                tmp = tmp[:index - 1] + [str(eval(''.join(tmp[index - 1:index + 2])))] + tmp[index + 2:]
        answer.append(abs(int(tmp[0])))
        print(answer)
    return max(answer)

print(solutiosn("100-200*300-500+20"))

print(solution("100-200*300-500+20"))