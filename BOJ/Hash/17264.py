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

for i in player_list:
    # score 점수 이상이 되면은 탈출하는 것이므로 리스트 안에 포함되어있는지로 보면 안된다.
    if result >= score:
        print("I AM NOT IRONMAN!!")
        sys.exit()
    if i in dic.keys():
        result += dic[i]
        if result <= 0:
            result = 0
    else:
        result = result - L
        if result <= 0:
            result = 0


# # print(list1)
# if score in list1:
#     print("I AM NOT IRONMAN!!")
# else:
print("I AM IRONMAN!!")