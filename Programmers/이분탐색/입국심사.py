n = 6
times = [7, 10]


def solution(n, times):
    answer = 0

    start = 1 # 최소범위
    end = max(times) * n # 최대범위

    while start <= end:
        mid = (start + end) // 2

        count = 0

        # 기본 입국심사 하는 틀
        for i in times:
            count += mid // i

        # 주어진 인원보다 더 많은 인원이 심사가 가능
        # 심사위원에게 주어진 시간 줄여보기
        if n <= count:
            answer = mid
            end = mid - 1

        # 주어진 인원보다 더 적은 인원을 심사했을 경우
        # 시간을 늘려보기
        else:
            start = mid + 1

    return answer


print(solution(n, times))