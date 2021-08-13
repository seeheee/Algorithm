# 최대힙 이용

import heapq
def solution(n, works):
    heap = []
    if sum(works) <= n:
        return 0

    for i in works:
        heapq.heappush(heap, -i)

    for _ in range(n):
        heapq.heapreplace(heap, heap[0] + 1)

    return sum(h**2 for h in heap)