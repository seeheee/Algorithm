def solution(max_weight, specs, names):
    dic = {}

    for n, w in specs:
        dic[n] = int(w)

    now = max_weight
    answer = 1
    for name in names:
        if dic[name] > now:
            answer += 1
            now = max_weight - dic[name]
        else:
            now -= dic[name]

    return answer