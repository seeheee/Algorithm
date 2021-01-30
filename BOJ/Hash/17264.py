# 이거 대체 왜 안되냐 ?

import sys
input = sys.stdin.readline

N, P = map(int, input().rstrip().split())
W, L, score = map(int, input().rstrip().split())

dic = {}
for _ in range(P):
    name, check = map(str, input().rstrip().split())
    if check == 'W':
        dic[name] = W
    elif check == 'L':
        dic[name] = -L


player_list = []
for _ in range(N):
    player = input().rstrip()
    player_list.append(player)

result = 0
list1 = []
for i in player_list:
    if i in dic.keys():
        result += dic[i]
        if result <= 0:
            result = 0
    else:
        if result - L <= 0:
            result = 0
        else:
            result = result - L
    list1.append(result)

print(list1)
if score in list1:
    print("I AM NOT IRONMAN!!")
else:
    print("I AM IRONMAN!!")