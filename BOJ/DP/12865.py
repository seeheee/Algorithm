# 평범함 배낭 (골드 5)
# 배낭문제로 무게가 소수라서 쪼갤수 있으면 분할가능 배낭문제, 쪼갤 수 없는 경우 0-1 배낭문제라고 한다.

N, K = map(int, input().split())

WV_list = [[0 for _ in range(K + 1)] for _ in range(N + 1)] # 1씩 더 하는 이유는 인덱스가 0일 경우의 초기화를 위해서 (5번 돈다)


Thing = [[0, 0]] # 따라서 여기서 기존의 N를 input로 받고 한개 더 필요하므로 0,0의 값이 들어가 줘야한다.
for _ in range(N):
    Thing.append(list(map(int, input().split())))

# [[0, 0], [6, 13], [4, 8], [3, 6], [5, 12]]

# 행렬을 계속 채워가는 것
for i in range(1, N+1):
    for j in range(1, K+1):
        weight = Thing[i][0]
        value = Thing[i][1]

        if j < weight: # 현재 무게(j)에서 담을 수 없을 시 전의 값을 그대로 가지고 오는 것, 어차피 안 담아져서 필요없음
            WV_list[i][j] = WV_list[i-1][j]
        else:
            WV_list[i][j] = max(value + WV_list[i-1][j-weight], WV_list[i-1][j])

# 가장 마지막의 값 출력
print(WV_list[N][K])



