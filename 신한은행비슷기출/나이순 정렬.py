# 문제를 제대로 안 읽어서 틀림.... 자꾸 왜 안되나 했는데 age를 정수로 출력해야 했었다,,,
# 그냥 정렬 문제
N = int(input())

online_list = list(list(input().split()) for _ in range(N))

online_list.sort(key=lambda x: int(x[0]))


for i in range(N):
    age, name = online_list.pop(0)
    print(age, name)



# for i in range(N):
#     heapq.heappush(online_list, input().split())
#
# print(online_list)
# for i in range(N):
#     print(online_list)
#     a, b = heapq.heappop(online_list)

