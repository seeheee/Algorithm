# 아예 로직을 어떻게 세워야 문제를 푸는지 감도 안 잡힘.....
# 문제 구현 로직이 너무 어려움
from collections import defaultdict


def solution(n, results):
    answer = 0
    # 딕서녀리로 연결리스트 설정
    win = defaultdict(set)
    lose = defaultdict(set)
    for i, j in results:
        win[i].add(j)
        lose[j].add(i)

    # 이기고 진 관계 표현
    for i in range(1, n + 1):
        # i에게 이긴 사람들은 i에게 이긴 사람들한테도 이긴거다.
        for winner in lose[i]:
            win[winner].update(win[i])
        # i에게 진 사람들은 i에게 진 사람들한테도 진 거다.
        for loser in win[i]:
            lose[loser].update(lose[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer