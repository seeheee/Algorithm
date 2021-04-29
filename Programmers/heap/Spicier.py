import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)

    for i in range(len(scoville)):
        if len(scoville) == 1:
            return -1
        new = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new)
        count += 1
        if check(scoville, K):
            break
    return count


def check(heap, K):
    for element in heap:
        if element < K:
            return False
    return True