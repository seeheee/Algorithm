import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

list1 = []
dic = {}
for _ in range(N):
    team = input().rstrip()
    member_count = int(input().rstrip())
    member = list(input().rstrip() for _ in range(member_count))
    member.sort()
    for i in member:
        dic[i] = team

for _ in range(M):
    q = input().rstrip()
    option = int(input().rstrip())

    if option == 1:
        print(dic[q])
    else:
        for k, j in dic.items():
            if j == q:
                print(k)


