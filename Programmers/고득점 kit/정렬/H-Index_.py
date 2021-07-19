# 문제 자체가 이해하기 어려움
# 간단히 풀 수 있는 방법 찾기, 아예 알고리즘 어떻게 세울지 생각을 못 함

# def solution(citations):
#     citations.sort()
#     c_len = len(citations)
#     for c in range(c_len):
#         if citations[c] >= c_len-c:  # 큰 값 하나만 리턴
#             return c_len-c
#     return 0

# 좀 더 직관적인 풀이
def solution(citations):
    citations.sort()
    l = len(citations)
    while True:
        for i, value in enumerate(citations):
            if value >= l and len(citations[i:]) >= l:
                return l
        else:
            l -= 1
            continue






print(solution([6, 5, 4, 1, 0]))