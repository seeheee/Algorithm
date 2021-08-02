# 정규표현식 sub는 첫번째 파라미터를 찾아서 두번째 파라미터로 변환, 세번째 파라미터는 해당 문자열
# bin()은 2진수를 만들고 결과는 문자열
# oct()는 8진수를 만들고 결과는 문자열
# hex()는 16진수를 만들고 결과는 문자열
import re
def solution(s):
    time, count = 0, 0
    while s != '1':
        count += s.count('0')
        a = ''.join(s.split('0'))
        s = bin(len(a))
        s = s[2:]
        time += 1
    answer = [time, count]
    return answer


# 정규표현식 사용
import re
def solution(s):
    time, count = 0, 0
    while s != '1':
        count += s.count('0')
        a = re.sub('0', '', s)
        s = bin(len(a))
        s = s[2:]
        time += 1
    answer = [time, count]
    return answer

print(solution("110010101001"))