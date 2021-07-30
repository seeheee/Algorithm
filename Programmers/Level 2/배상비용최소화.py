import heapq

def solution(no, works):
    heap = []

    if sum(works) < no:
        return 0

    for i in works:
        heapq.heappush(heap, -i)

    for _ in range(no):
        heapq.heapreplace(heap, heap[0] + 1)

    return sum([i ** 2 for i in heap])

print(solution(3, [1,1,1]))