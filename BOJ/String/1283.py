from collections import deque

N = int(input())

word = []
check = deque()
for _ in range(N):
    in1 = input().split()
    word.append(in1)
    print(word)
for i in word:
    if i[0][0].capitalize() not in check:
        check.append(i[0][0].capitalize())
    # elif i[0][1].capitalize()  not in check:
    #     check.append(i[0][0].capitalize())
    print(check)