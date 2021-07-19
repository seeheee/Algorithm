import heapq

jobs = [[1, 6], [4, 3], [5, 2]]

def solution(jobs):
    heap1 = []
    now = 0
    j = 0
    start = -1
    answer = 0
    # 현재 시점과 총 대기 시간을 구한다.
    # 현재시점: now
    # 총 대기시점: answer
    # 바로 이전에 완료한 작업의 시작시간: start

    while j < len(jobs):
        for i in range(len(jobs)):
            # 현재 수행중 가능한지 확인
            if jobs[i][0] <= now and jobs[i][0] > start:
                heapq.heappush(heap1, [jobs[i][1], jobs[i][0]])

        # 힙이 있다는 것은 현재 시점에서 작업이 가능하다는 것
        if heap1:
            # current[1]이 소요시간 , current[0]이 바로 이전에 완료한 작업의 시작시간
            current = heapq.heappop(heap1)
            start = now
            now = now + current[0]
            answer = answer + (now - current[1])
            # if문을 한번 돌면 작업 한 개 완료
            j += 1
        # 힙이 없다면 현재 시점에서 작업 불가능
        else:
            now += 1
    return int(answer/len(jobs))





solution(jobs)