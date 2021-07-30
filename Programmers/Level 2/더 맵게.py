import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        if scoville[0] < K and len(scoville) == 1:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        mix = first + (second * 2)
        heapq.heappush(scoville, mix)
        answer += 1
        if scoville[0] >= K:  # 맨 처음에 min 함수 사용했더니 효율성에서 시간초과(min - O(n))
            return answer



from collections import deque
# import heapq
# def solution(scoville, K):
#     scoville.sort()
#     answer = 0
#     if min(scoville) >= K:
#         return answer
#     if max(scoville) <= K:
#         return -1
#
#     while scoville:
#         scoville.sort()
#         first = scoville.pop(0)
#         second = scoville.pop(0)
#         if first > second:
#             first, second = second, first
#         new = first + (second * 2)
#         scoville.append(new)
#         answer += 1
#
#         if min(scoville) >= K:
#             return answer
#         if max(scoville) <= K:
#             return -1


