# 조건문을 나누는 것이 어려웠음
import heapq
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

def solution(operations):
    heap = [] # 최소값을 담을 힙
    Max_heap = [] # 최대값을 담을 힙

    for operation in operations:
        if operation.startswith('I'):
            result = operation.split()
            heapq.heappush(heap, int(result[1])) #넣어줄때 애초에 int로 넣으면 됨
            heapq.heappush(Max_heap, (int(result[1]) * -1, int(result[1]))) # 이렇게 넣어주면 for문 필요없음(int(result[1]) * -1)
        else:
            # 문제 요구
            if len(heap) == 0:
                pass

            elif operation.startswith('D 1'):
                max_value = heapq.heappop(Max_heap)[1]
                heap.remove(max_value)

            elif operation.startswith('D -1'):
                heapq.heappop(heap)

    # 모든 연산을 처리한 후에 최대값과 최소값 출력
    if heap:
        answer = [heapq.heappop(Max_heap)[1], heapq.heappop(heap)]
        return answer
    else:
        return [0,0]


print(solution(operations))