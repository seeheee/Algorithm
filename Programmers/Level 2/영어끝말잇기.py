# 리스트를 하나 더 만들어서 그 리스트와 주어진 배열을 비교하면서 문제를 풀어야함
# 안 그럴시(startswith 사용) for문이 여러개 필요하고 이전에 나온 글자 처리하는 것이 어려움..

def solution(n, words):
    speek_list = []
    for i in range(len(words)):
        if not speek_list:
            speek_list.append(words[i])
        else:
            if len(words[i]) == 1:
                return [(i%n)+1, (i//n)+1]
            elif words[i] in speek_list:
                return [(i%n)+1, (i//n)+1]
            elif speek_list[i-1][-1] != words[i][0]:
                return [(i%n)+1, (i//n)+1]
            else:
                speek_list.append(words[i])
    return [0,0]

ha = "tank"

print(ha[-1:])
print(ha[:1])