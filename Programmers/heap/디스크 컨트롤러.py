import heapq
import copy

jobs = [[1, 6], [4, 3], [5, 2], [6, 1]]
jobs_copy = copy.copy(jobs)
time = 0

heap1 = []
sum1 = 0
heap2 = []

def solution(jobs):
    time = 0
    sum1 = 0

    while heap1:
        # 작업을 수행하고 있지 않을 때
        if time == 0 or time < jobs[0][1]:
            heapq.heapify(jobs)
            result = heapq.heappop(jobs)
            for i in result:
                sum1 += i
            time = sum1

        # 작업을 수행하고 있을 때
        else:
            for i in range(len(jobs)):
                heapq.heappush(heap1, [jobs[i][1], jobs[i][0]])
            result = heapq.heappop(heap1)
            for i in result:
                sum1 += i
            time = sum1




solution(jobs)