def solution(s):
    answer = ''
    words = s.split(' ')
    for word in words:
        for idx, w in enumerate(word):
            if idx == 0:
                answer += w.upper()
            else:
                answer += w.lower()
        answer += ' '
    return answer[:-1]
