import sys
input = sys.stdin.readline
N = int(input().rstrip())

stair = []
for _ in range(N):
    in1 = int(input().rstrip())
    stair.append(in1)

D = []


# 계단의 길이가 한 개거나 두 개인 경우도 나눠서 생각해야 함(안그러면 인덱스 에러)

if len(stair) == 1:
    D.append(stair[0])
    print(D.pop())
elif len(stair) == 2:
    D.append(stair[0])
    D.append(max(stair[1], stair[0] + stair[1]))
    print(D.pop())
else:
    # 초기값 설정
    # 한번에 두 칸 밟았을 때 or 한 번에 한 칸 씩 밟았을 때
    D.append(stair[0])
    D.append(max(stair[1], stair[0] + stair[1]))
    D.append(max(stair[1] + stair[2], stair[0] + stair[2]))

    for i in range(3, len(stair)):
        result = max(stair[i] + stair[i-1] + D[i-3], stair[i] + D[i-2])
        D.append(result)
    print(D.pop())