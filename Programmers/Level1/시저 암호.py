def solution(s, n):
    Alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SAlpha = 'abcdefghijklmnopqrstuvwxyz'
    A_list = list(map(str, Alpha))
    S_list = list(map(str, SAlpha))
    answer = []
    for i in range(len(A_list)):
        for j in s:
            if j in A_list[i]:
                answer.append(A_list[i+n])
            elif j in S_list[i]:
                answer.append(S_list[i+n])
            elif j == ' ':
                continue
    return answer