# 흐름 생각하기 너무 어려웠음...

def solution(progresses, speeds):
    result, day = 0, 0
    answer = []

    while progresses:
        if progresses[0] + day*speeds[0] >= 100: # 리스트로가 아니라 day를 곱해주는 방식
            progresses.pop(0)
            speeds.pop(0)
            result += 1
        else:
            if result > 0:  # count가 있다면 리스트에 담아주고 다음을 위해 초기화
                answer.append(result)
                result = 0
            day += 1
    answer.append(result)
    return answer


# zip을 이용하는 방식

def solution(progresses, speeds):
    q = []
    for p,c in zip(progresses,speeds):
        if len(q) == 0 or q[-1][0] < -((p-100)//c):
            q.append([-((p-100)//c), 1])
            print(q)
        else:
            q[-1][1] += 1
            print("count 더해주기", q)
    return [i[1] for i in q]

# def solution(progresses, speeds):
#     day = 0
#     count = 0
#     tmp = []
#
#     while progresses[0] < 100:
#         for i in range(len(progresses)):
#             progresses[i] = progresses[i] + speeds[i]
#             day += 1
#             c = day // 3
#             print(c)
#
# print(solution([93,30,55],[1,30,5]))




