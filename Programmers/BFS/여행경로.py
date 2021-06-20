# 엄청 어려워... 어려워...
from collections import defaultdict

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
visited = [0 for _ in range(len(tickets) + 1)]


def solution(tickets):

    # 인접 리스트 구현(딕셔너리로 구현) - 인접 행렬 방법 밖에 몰랐음
    def link_list():
        dic = defaultdict(list)
        for key, ticket in tickets:
            dic[key] = ticket
        return dic

    def dfs():



    routes = link_list()
    print(routes)

    # for r in routes:
    #     #     routes[r].sort()
    #     #
    #     # print(routes)

    answer = dfs()
    return answer

print(solution(tickets))

