
# DP 문제
def solution(land):
    r = len(land)
    c = len(land[0])
    visited = [[0*c] for _ in range(r)]
    answer = []
    for i in range(r):
        for j in range(c):
            if visited[i][j] == 0: # 인덱스 에러 뜨는데 이유를 모르겠음
                if max(land[i]) == land[i][j]:
                    visited[i][j] = 1
                    visited[i+1][j] = 1
                    del land[i+1][j]
                    answer.append(max(land[i]))
                else:
                    visited[i][j] = 1
    return answer

# 직관적인 풀이 방식(제한 4열이 아닐 경우)
def solutionss(land):
    r = len(land)
    c = len(land[0])
    for i in range(1, r):
        land[i][0] = max(land[i-1][1],land[i-1][2],land[i-1][3]) + land[i][0]
        land[i][1] = max(land[i-1][0],land[i-1][2],land[i-1][3]) + land[i][1]
        land[i][2] = max(land[i-1][1],land[i-1][0],land[i-1][3]) + land[i][2]
        land[i][3] = max(land[i-1][1],land[i-1][2],land[i-1][0]) + land[i][3]
    return max(land[len(land)-1])

# 최종 문제풀이(시간복잡도 n)
def solutions(land):
    r = len(land)
    c = len(land[0])
    for i in range(1, r):
        for j in range(c):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
            print(land[i][j])  # 10, 11, 12, 11, 16, 15, 13, 13
    return max(land[len(land)-1])




print(solutions([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))