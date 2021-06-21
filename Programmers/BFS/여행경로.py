# 엄청 어려워... 어려워...
# 얘는 bfs(최단거리, 큐) -> dfs(경로 특징, 스택/재귀)

from collections import defaultdict

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]


def solution(tickets):
    # 인접 리스트 구현(딕셔너리로 구현) - 인접 행렬 방법 밖에 몰랐음
    # {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
    def link_list():
        dic = defaultdict(list)
        for key, ticket in tickets:
            dic[key].append(ticket)
        return dic

    # 이 방법으로 하면은 리스트가 아니라서 정렬 안 됨
    # {'ICN': 'JFK', 'HND': 'IAD', 'JFK': 'HND'}
    # def link_list2():
    #     #     dic = defaultdict(list)
    #     #     for key, ticket in tickets:
    #     #         dic[key] = ticket
    #     #     return dic

    # 다 한번 쭉 돌아서 stack 경로 담고 그 다음에 확인하면서 path에 담는다.
    def dfs():
        stack = ['ICN']
        path = []
        while stack:
            top = stack[-1]
            # 특정 공항이 없거나 공항이 있어도 그 공항에서 인접한 아이가 없다.
            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                # 모든 인접한 아이들 전부 확인
                stack.append(routes[top].pop(0))
        return path[::-1]

    routes = link_list()

    # 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
    # {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
    for r in routes:
        routes[r].sort()  # 딕셔너리 value 값을 기준으로 sort / link_list2 함수로 할 시 오류 발생
    print(routes)

    return dfs()



print(solution(tickets))


