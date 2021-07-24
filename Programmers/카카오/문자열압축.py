def solution(msg):
    answer = []
    index_dic = {}
    for i in range(1, 27):
        index_dic[i] = chr(i + 64)

    for m in range(len(msg)-1):
        if index_dic[m+1]:
            answer.append(m+1)
            print(answer)
        else:
            index_dic[m+27] = msg[m]+msg[m+1]
            print(index_dic)


print(solution("KAKAO"))