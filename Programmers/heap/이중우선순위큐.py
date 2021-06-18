import heapq
operations = ["I 16","D 1"]


def solution(operations):
    heap = []

    for operation in operations:
        if operation.startswith('I'):
            result = operation.split()
            heap.append(result[1])

    new_heap = list(map(int, heap))
    print(new_heap)

    while new_heap:
        for operation in operations:
            if operation.startswith('D 1'):
                for i in new_heap:
                    heapq.heappush(new_heap, (-i, i))
                heapq.heappop(new_heap)

            if operation.startswith('D -1'):
                heapq.heapify(new_heap)
                heapq.heappop(new_heap)

    # 큐가 비어있으면 [0,0] 리턴
    while not new_heap:
        return [0,0]

    answer = sorted(new_heap, reverse=True)
    return answer


print(solution(operations))