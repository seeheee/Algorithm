# 과제는 끝나지 않아 !
# 마지막 점수가 0이 되어야 과제가 끝난다 -> time의 pop에서 1을 뺀다.

from collections import deque
import sys
input = sys.stdin.readline
score = deque()
time = deque()
answer = deque()

N = int(input())

for i in range(N):
    list1 = list(map(int, input().split()))
    if list1[0] == 1:
        score.append(list1[1])
        time.append(list1[2])
    if time:
        time[-1] = time[-1] - 1
        if time[-1] == 0:
            time.pop()
            answer.append(score.pop())
print(sum(answer))
