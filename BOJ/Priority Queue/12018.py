# 연세 토토 (실버 3)
import heapq

heap = []
count = 0
N, M = map(int, input().split())

for i in range(N):
    p, L = map(int, input().split())
    miles_list = list(map(int, input().split()))
    if p >= L:
        heapq.heapify(miles_list)
        # 인덱스 K번째 최소값 구하기 (이 부분 생각 못하고 전부 최소값으로 주었음)
        # 인덱스 0번을 구할려면 1번은 돌아야함
        # 3번 돌면 인덱스 2번째 추출 (따라서 1을 더해줘야 함)
        for i in range(abs(L-p)+1):
            answer = heapq.heappop(miles_list)
            # print("miles_list", miles_list)
        heapq.heappush(heap, answer)
    else:
        # 수강인원보타 신청인원이 적을 경우 마일리지 1 설정
        heapq.heappush(heap, 1)

# print("heap", heap)

while heap:
    result = heapq.heappop(heap)
    if M - result >= 0:
        count += 1
        M = M - result
    else:
        break
print(count)
