def solution(lottos, win_nums):
    answer = []
    prior = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    count = 0
    for l in lottos:
        for w in win_nums:
            if l == w:
                count += 1
    answer.append(prior[count])

    for l in lottos:
        if l == 0:
            count += 1
    answer.append(prior[count])
    answer.sort()
    return answer