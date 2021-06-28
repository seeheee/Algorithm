def solution(strings, n):
    # a = sorted(str_list)
    # a.sort(key=lambda x: x[n])
    # return a

    # 사전순으로 먼저 정렬하고 인덱스 n으로 하는거다
    return sorted(sorted(strings), key=lambda x: x[n])






print(solution(["abce", "abcd", "cdx"], 2))