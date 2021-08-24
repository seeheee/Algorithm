def solution(land):

    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][j+1:] + land[i-1][:j])

    return max(map(max, land))