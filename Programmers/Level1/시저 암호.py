# 문자열 굳이 리스트에 담을 필요 없고 그냥 문자열 더하기 가능

def solution(s, n):
    Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SAlpha = 'abcdefghijklmnopqrstuvwxyz' # 25개의 원소 배열
    answer = ''
    for j in s:
        if j in Alpha:
            idx = Alpha.find(j)
            answer += Alpha[(idx+n)%26]
        elif j in SAlpha:
            idx = SAlpha.find(j)
            answer += SAlpha[(idx+n)%26]
        elif j == ' ':
            answer += ' '
    return answer