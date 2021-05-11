# 크리스마스 선물(실버 3)
import heapq

N = int(input())
heap = []
for i in range(N):
    input_value = input() # 변수로 담아야 이거를 또 쓸 수 있음(즉 입력을 한번만 받아야 함)
    if input_value == '0': # 아이를 만났으니
        if heap: # 선물이 있는 거
            print(heapq.heappop(heap)[1])
        else: # 선물이 없는 거
            print("-1")
    else:
        present = list(map(int, input_value.split()))
        print("present", present)
        for item in range(1, len(present)):
            heapq.heappush(heap, (-present[item], present[item]))
            print("heap", heap)


# 잘못된 코드
import heapq

N = int(input())
heap = []
for i in range(N):
    if input() == '0':
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print("-1")
    else:
        # input이 0이 아니면 다시 input을 받아와서 "0이 아닌 input이 사라짐"
        # 그래서 present에 2 3 2 다음 값인 0이 담긴 거였다.
        present = list(map(int, input().split()))
        for item in range(1, len(present)):
            heapq.heappush(heap, (-present[item], present[item]))


