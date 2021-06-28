# # 문자열에 공백이 있어서 이를 출력하고 싶다.
# s = "try helllo world     try"
# s_split = s.split(' ')
# print(s_split)
# # ['try', 'helllo', 'world', '', '', '', '', 'try']
#
#
s = "try helllo world     try"
# s_split = s.split()
# print(s_split)
# # s_split = ['try', 'hello', 'world']

def solution(s):
    words = s.split(' ')
    print(words)
    answer = ''
    for word in words:
        for idx, w in enumerate(word):
            if idx % 2 == 0:
                answer += w.upper()
            else:
                answer += w.lower()

        answer += ' '
    return answer[:-1]


print(solution(s))

